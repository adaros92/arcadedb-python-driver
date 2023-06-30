from pyarcade.api.client import Client

import json
import logging
import requests


class SyncClient(Client):
    def __init__(self, host: str, port: str, protocol: str = "http", **kwargs):
        super().__init__(host, port, protocol, **kwargs)

    def post(self, endpoint: str, payload: dict) -> requests.Response:
        endpoint = self._get_endpoint(endpoint)
        logging.info(f"posting to {endpoint} with payload {payload}")
        response = requests.post(
            endpoint,
            data=json.dumps(payload),
            headers=self.headers,
            auth=(self.username, self.password),
        )
        response.raise_for_status()
        logging.debug(f"response: {response.text}")
        return response

    def get(self, endpoint: str) -> requests.Response:
        endpoint = self._get_endpoint(endpoint)
        logging.info(f"submitting get request to {endpoint}")
        response = requests.get(
            endpoint,
            auth=(self.username, self.password),
        )
        logging.debug(f"response: {response.text}")
        response.raise_for_status()
        return response
