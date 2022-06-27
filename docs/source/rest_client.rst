Rest Client API
===============

Overview
--------

The Rest Client interfaces with `HTTP API <https://docs.sandbox.poloniex.com/#http-api>`_ and provides read access to public market data through the public endpoints and read / write access to your private account via the private endpoints.

Initialize Client
-----------------

.. code:: python

    from polosdk import RestClient, RequestError

    api_key = '<YOUR_API_KEY>'
    api_secret = '<YOUR_API_SECRET>'

    def main():
        polo_rest = RestClient(api_key, api_secret)

        # get account balances
        try:
            response = polo_rest.accounts().get_balances()
            print(response)
        except RequestError as request_error:
            print(request_error)


    if __name__ == '__main__':
        main()