class Client:
    """
    Main REST client used for accessing test.

    """
    def __init__(self, api_key=None, api_secret=None, url=None):
        """
        Args:
            api_key (str, required): ...
            api_secret (str, required): ...
            url (str, optional): ...
        """

    def get_timestamp(self):
        """
        Get current server time.

        Returns:
            A json object with server time.
            {
                'serverTime': (int) Server time
            }

        Raises:
            RequestError: An error occurred communicating with trade engine.
        """
        pass
