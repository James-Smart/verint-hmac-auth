import base64
import datetime
import hmac
from hashlib import sha256
from requests.auth import AuthBase
import os
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode


def _get_current_timestamp():
    # Return current UTC time in ISO8601 format
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _base64url(input_bytes):
    base64_string = base64.b64encode(input_bytes).decode('utf-8')
    return base64_string.replace('=', '').replace('+', '-').replace('/', '_')


class VerintHmac(AuthBase):
    API_KEY_QUERY_PARAM = 'apiKey'
    SIGNATURE_HTTP_HEADER = 'Authorization'
    TIMESTAMP_HTTP_HEADER = 'X-Auth-Timestamp'
    VERSION_HTTP_HEADER = 'X-Auth-Version'
    SIGNATURE_DELIM = '\n'
    VERSION_1 = '1'
    SIGNATURE_PREFIX = 'Vrnt-1-HMAC-SHA256'

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        self._encode(request)
        return request

    def _encode(self, request):
        timestamp = _get_current_timestamp()
        self._add_signature(request, timestamp)
        request.headers['Content-Type'] = 'application/json'


    def _add_signature(self, request, timestamp):
        method = request.method
        path = request.path_url
        content = request.body or ''
        salt = _base64url(os.urandom(16))
        string_to_sign = f'{salt}\n{method}\n{path}\n{timestamp}\n{content}\n'
        signature = self._sign(string_to_sign)
        auth_header_value = f'{VerintHmac.SIGNATURE_PREFIX} salt={salt},iat={timestamp},kid={self.api_key},sig={signature}'
        request.headers[VerintHmac.SIGNATURE_HTTP_HEADER] = auth_header_value


    def _sign(self, string_to_sign):
        #digest = hmac.new(key=bytearray(self.secret_key, 'utf-8'), msg=bytearray(string_to_sign, 'utf-8'), digestmod=sha256).digest()
        hash = hmac.new(base64.b64decode(self.secret_key),string_to_sign.encode('utf-8'),sha256)
        return _base64url(hash.digest())
