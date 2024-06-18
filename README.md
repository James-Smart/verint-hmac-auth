# verint-hmac-auth

Vertint HMAC authentication for Python client libraries.

This library makes it easy to add support for Verint HMAC authentication in Python.
It works by providing a custom authenticator for the requests library.

## Getting Started
To install:

```python
pip install verint-hmac-auth
```

In your code, import the `VerintHmac` class and specify it on the `auth` parameter when issuing API calls:

```python
import requests
from verint_hmac_auth import VerintHmac

response = requests.get('http://example.com/api', auth=VerintHmac('your_api_key', 'your_secret_key'))
```



This library is based on bazaarvoice/python-hmac-aut

