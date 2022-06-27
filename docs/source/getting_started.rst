Getting Started
===============

Installation
------------

``polo-sdk-python`` is available on `PYPI <https://pypi.python.org/pypi/polo-sdk-python/>`_.
Install with ``pip``:

.. code:: bash

    pip install polo-sdk-python

Sign Up
-------

If you do not have a Poloniex account yet, use the `link <https://poloniex.com/signup/>`_ to sign up.

Create an API Key
-----------------

Once you are verified and have an account, you can create an API Key.

Enabling IP address restrictions for API keys is strongly recommended. Withdrawals are disabled by default and must be enabled on a per key basis.

As the name implies, your secret must remain private! If you suspect your key has been compromised, immediately disable that key and generate a new one.

Minimize Latency
----------------

If you will be performing high-frequency trading, you may wish to locate your bots as close to our servers as possible. As Poloniex uses Cloudflare for all requests, you can minimize network latency by positioning your client near the Cloudflare gateway in Dublin, Ireland. You can identify which Cloudflare gateway your client is accessing by running this command on the same machine as your bot:

curl -s https://www.cloudflare.com/cdn-cgi/trace

Cloudflare’s Dublin data center will return a “colo” field of “DUB”. If you get a different “colo” value, you can look up the location at https://www.cloudflarestatus.com.

Rate Limits
-----------

- All cancel requests are limited to 2000 per second

- All other requests - 6 per second
