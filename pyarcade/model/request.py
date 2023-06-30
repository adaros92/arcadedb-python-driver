from dataclasses import dataclass


@dataclass
class RequestData:
    endpoint: str
    command: str
    language: str = "sql"

    def payload(self) -> dict:
        if not self.language:
            return {"command": self.command}
        else:
            return {"command": self.command, "language": self.language}
