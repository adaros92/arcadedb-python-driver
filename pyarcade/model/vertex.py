from dataclasses import dataclass

from pyarcade.model.bucket import Bucket
from pyarcade.model.record import Record
from pyarcade.model.type import Type


@dataclass
class Vertex:
    name: str
    type: Type
    record: Record = None
    bucket: Bucket = None

    def rid(self) -> str:
        return self.record.rid()

