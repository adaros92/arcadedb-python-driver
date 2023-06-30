import pytest
import requests

from pyarcade.api.sync import SyncClient


def test_sync_client_instantiation():
    client = SyncClient(
        host="localhost", port="2480", username="root", password="playwithdata"
    )
    assert client.host == "localhost"
    assert client.port == 2480
    assert client.protocol == "http"
    assert client.url == "http://localhost:2480"
    assert client.username == "root"
    assert client.password == "playwithdata"
    assert client.headers == {"Content-Type": "application/json"}
    assert str(client) == "<host=localhost port=2480 user=root>"
    assert repr(client) == str(client)


def test_sync_client_get():
    endpoint = "/api/v1/server"
    client = SyncClient(
        host="localhost", port="2480", username="root", password="playwithdata"
    )
    with pytest.raises(requests.exceptions.ConnectionError):
        client.get(endpoint)


def test_sync_client_post():
    endpoint = "/api/v1/server"
    client = SyncClient(
        host="localhost", port="2480", username="root", password="playwithdata"
    )
    with pytest.raises(requests.exceptions.ConnectionError):
        client.post(endpoint, payload={})
