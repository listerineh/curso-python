import json
from typing import Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: str
    description: str
    created_at: datetime
    updated_at: datetime

    def __init__(
        self, 
        description: str, 
        id: str, 
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.description = description
        self.created_at = datetime.now() if not created_at else created_at
        self.updated_at = datetime.now() if not updated_at else updated_at

    def to_dict(self) -> dict:
        return json.dumps(
            {
                "id": self.id,
                "description": self.description,
                "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
