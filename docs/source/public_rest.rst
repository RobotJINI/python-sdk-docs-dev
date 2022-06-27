Public REST API Methods
=======================

The public REST API allows read access to public market data.

No authentication is necessary but you must not excessively use any API endpoint.

timestamp
-----------

.. code:: python

    response = client.get_timestamp()
    print(response)
