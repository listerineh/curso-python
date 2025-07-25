from abc import ABC
from typing import List

from src.core.domain.todo import Todo


class TodoPort(ABC):
    @classmethod
    def get_all(self) -> List[Todo]:
        pass

    @classmethod
    def create(self, new_todo: Todo) -> bool:
        pass

    @classmethod
    def update(self, id: str, new_data: Todo) -> bool:
        pass

    @classmethod
    def delete(self, id: str) -> bool:
        pass

    @classmethod
    def exists(self, id: str) -> bool:
        pass
