from pyarcade.api import config


def test_api_config_generation():
    assert config.ARCADE_BASE_ENDPOINT == "/api/v1"
    assert config.ARCADE_BASE_SERVER_ENDPOINT == "/api/v1/server"
    assert config.ARCADE_BASE_EXISTS_ENDPOINT == "/api/v1/exists"
    assert config.ARCADE_BASE_COMMAND_ENDPOINT == "/api/v1/command"
    assert config.API_RETRY_MAX == 3
    assert config.API_RETRY_DELAY == 1
    assert config.API_RETRY_BACKOFF == 2
