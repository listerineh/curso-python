from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: str
    description: str
    #created_at: datetime
    #updated_at: datetime
