from dataclasses import dataclass

from pyarcade.model.bucket import Bucket


@dataclass
class Record:
    bucket: Bucket
    record_position: str

    def rid(self) -> str:
        return f"#{self.bucket.id}:{self.record_position}"
