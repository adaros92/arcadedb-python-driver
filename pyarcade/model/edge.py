from dataclasses import dataclass

from pyarcade.model.bucket import Bucket
from pyarcade.model.type import Type
from pyarcade.model.vertex import Vertex


@dataclass
class Edge:
    name: str
    bucket: Bucket
    type: Type
    from_vertex: Vertex = None
    to_vertex: Vertex = None
