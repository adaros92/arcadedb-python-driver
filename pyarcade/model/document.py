from dataclasses import dataclass

from pyarcade.model.type import Type


@dataclass
class Document:
    name: str
    type: Type

