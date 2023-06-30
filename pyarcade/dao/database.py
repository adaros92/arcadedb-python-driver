import logging
import requests

from typing import Union

from pyarcade.api.client import Client
from pyarcade.api import config
from pyarcade.model.request import RequestData
from pyarcade.model.database import Database


class DatabaseDao:
    def __init__(
        self,
        client: Client,
        mutation_endpoint: str = config.ARCADE_BASE_SERVER_ENDPOINT,
        exists_endpoint: str = config.ARCADE_BASE_SERVER_ENDPOINT,
    ):
        self.client = client
        self.mutation_endpoint = mutation_endpoint
        self.exists_endpoint = exists_endpoint

    def _db_exists(self, name: str) -> bool:
        response = self.client.get(f"{self.exists_endpoint}/{name}")
        return response.json()["result"]

    def get_db(self, name: str) -> Database:
        db_exists = self._db_exists(name)
        if db_exists:
            return Database(name, exists=True)
        else:
            return Database(name, exists=False)

    def create_db(self, name: str) -> Union[None, requests.Response]:
        db = self.get_db(name)
        if db.exists:
            logging.info(f"Database {name} already exists")
            return None
        request_data = RequestData(
            endpoint=self.mutation_endpoint,
            command=f"create database {name}",
            language=None,
        )
        try:
            return self.client.post(request_data.endpoint, request_data.payload())
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400 and "already exists" in e.response.text:
                logging.info(f"Database {name} already exists")
            else:
                raise
