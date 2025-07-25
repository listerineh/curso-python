from dataclasses import dataclass
import json


@dataclass
class User:
    id: str
    full_name: str
    email: str

    def to_dict(self) -> dict:
        return json.dumps(**self)
