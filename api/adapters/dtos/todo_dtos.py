from datetime import datetime
from typing import Union
from dataclasses import dataclass

from api.core.domain.todo import Todo


@dataclass
class TodoPostRequest:
    id: str
    description: str

    def parse(self) -> Todo:
        return Todo(description=self.description, id=self.id)


@dataclass
class TodoPutRequest:
    id: str
    description: str

    def parse(self) -> Union[str, Todo]:
        return self.id, Todo(
            description=self.description, 
            id=self.id, 
            updated_at=datetime.now()
        )

@dataclass
class TodoDeleteRequest:
    id: str

    def parse(self) -> Todo:
        return Todo(id=self.id)