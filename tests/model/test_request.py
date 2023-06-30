from pyarcade.model.request import RequestData


def test_request_data():
    request = RequestData("endpoint", "command", "language")
    assert request.endpoint == "endpoint"
    assert request.command == "command"
    assert request.language == "language"
    assert request.payload() == {"command": "command", "language": "language"}
    request = RequestData("endpoint", "command")
    assert request.endpoint == "endpoint"
    assert request.command == "command"
    assert request.language == "sql"
    assert request.payload() == {"command": "command", "language": "sql"}
