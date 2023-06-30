import os


def _get_env_variable(key: str, default: str = None) -> str:
    return os.environ.get(key, os.getenv(key, default))


ARCADE_BASE_ENDPOINT = _get_env_variable("ARCADE_API_ENDPOINT", "/api/v1")
ARCADE_BASE_SERVER_ENDPOINT = f"{ARCADE_BASE_ENDPOINT}/server"
ARCADE_BASE_EXISTS_ENDPOINT = f"{ARCADE_BASE_ENDPOINT}/exists"
ARCADE_BASE_COMMAND_ENDPOINT = f"{ARCADE_BASE_ENDPOINT}/command"

API_RETRY_MAX = int(_get_env_variable("ARCADE_API_RETRY_MAX", "3"))
API_RETRY_DELAY = int(_get_env_variable("ARCADE_API_RETRY_DELAY", "1"))
API_RETRY_BACKOFF = int(_get_env_variable("ARCADE_API_RETRY_BACKOFF", "2"))
