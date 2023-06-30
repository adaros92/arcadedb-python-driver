from pyarcade.api.client import Client

import retry


class SyncClient(Client):

    def __init__(self, host: str, port: str, protocol: str = "http", **kwargs):
        super().__init__(host, port, protocol, **kwargs)

    @rety
    def post(self, endpoint):
        pass

    def get(self, endpoint):
        pass
