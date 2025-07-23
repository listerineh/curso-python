from typing import List
from src.core.domain.todo import Todo
from src.core.ports.todo_port import TodoPort


class InMemoryTodoRepository(TodoPort):
    def __init__(self) -> None:
        super().__init__()
        self.todos = []

    def get_all(self) -> List[Todo]:
        return self.todos

    def create(self, new_todo: Todo) -> bool:
        self.todos.append(new_todo)
        return True

    def exists(self, id: str) -> bool:
        for todo in self.todos:
            if todo.id == id:
                return True

        return False


class PostgresTodoRepository(TodoPort):
    pass


class FirebaseTodoRepository(TodoPort):
    pass