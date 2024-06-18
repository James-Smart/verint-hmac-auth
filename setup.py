from setuptools import setup


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


setup(
    name='verint-hmac-auth',
    version='0.5',
    description='Python client for verint hmac authentication (Vrnt-1-HMAC-SHA256)',
    long_description=read('README.md'),
    url='',
    license=read('LICENSE'),
    author='James Smart',
    author_email='',
    packages=['verint_hmac_auth'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['requests']
)
