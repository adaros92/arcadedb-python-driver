from pyarcade.api import config
from abc import ABC, abstractmethod

import logging
import requests

from retry import retry


class Client(ABC):
    def __init__(self, host: str, port: str, protocol: str = "http", **kwargs):
        self.host = host
        self.port = int(port)
        self.kwargs = kwargs
        self.protocol = protocol
        self._validate()

    def _validate(self):
        if not self.host:
            raise ValueError("Host is required")
        if not self.port:
            raise ValueError("Port is required")

    def _get_endpoint(self, endpoint: str) -> str:
        if endpoint.startswith("/"):
            endpoint = endpoint[1:]
        if self.url.endswith("/"):
            return f"{self.url}{endpoint}"
        else:
            return f"{self.url}/{endpoint}"

    @property
    def headers(self):
        default = "application/json"
        key = "content_type"
        if key not in self.kwargs:
            logging.warning(f"No content type, defaulting to {default}")
        content_type = self.kwargs.get(key, default)
        return {"Content-Type": content_type}

    @property
    def url(self) -> str:
        return f"{self.protocol}://{self.host}:{self.port}"

    @property
    def username(self) -> str:
        return self.kwargs.get("username") or self.kwargs.get("user")

    @property
    def password(self) -> str:
        return self.kwargs.get("password") or self.kwargs.get("pw")

    def __repr__(self) -> str:
        return f"<host={self.host} port={self.port} user={self.username}>"

    def __str__(self) -> str:
        return self.__repr__()

    @abstractmethod
    @retry(
        tries=config.API_RETRY_MAX,
        delay=config.API_RETRY_DELAY,
        backoff=config.API_RETRY_BACKOFF,
    )
    def post(self, endpoint: str, payload: dict) -> requests.Response:
        pass

    @abstractmethod
    @retry(
        tries=config.API_RETRY_MAX,
        delay=config.API_RETRY_DELAY,
        backoff=config.API_RETRY_BACKOFF,
    )
    def get(self, endpoint: str) -> requests.Response:
        pass
