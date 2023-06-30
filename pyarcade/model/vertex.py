from dataclasses import dataclass

from pyarcade.model.bucket import Bucket
from pyarcade.model.type import Type


@dataclass
class Vertex:
    name: str
    type: Type
    rid: str = None
    bucket: Bucket = None

