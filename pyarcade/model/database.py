from dataclasses import dataclass


@dataclass
class Database:
    name: str
    exists: bool
