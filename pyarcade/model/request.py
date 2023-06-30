from dataclasses import dataclass

from typing import Union


@dataclass
class RequestData:
    endpoint: str
    command: Union[str, None] = None
    language: Union[str, None] = "sql"

    def payload(self) -> dict:
        if not self.language:
            return {"command": self.command}
        else:
            return {"command": self.command, "language": self.language}
