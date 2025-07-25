import psycopg2
from typing import List

from psycopg2.extensions import cursor

from src.adapters.utils.env_manager import get_settings
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

    def update(self, id: str, new_data: Todo) -> bool:
        for i in range(len(self.todos)):
            if self.todos[i].id == id:
                self.todos[i].description = new_data.description
                self.todos[i].updated_at = new_data.updated_at
                return True

        return False

    def delete(self, id: str) -> bool:
        for todo in self.todos:
            if todo.id == id:
                self.todos.remove(todo)
                return True
        return False

    def exists(self, id: str) -> bool:
        for todo in self.todos:
            if todo.id == id:
                return True

        return False


class PostgresTodoRepository(TodoPort):
    def __init__(self):
        settings = get_settings()

        try:
            self.connection = psycopg2.connect(
                dbname=settings.postgres_dbname,
                user=settings.postgres_user,
                password=settings.postgres_password,
                host=settings.postgres_host,
                port=settings.postgres_port,
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            raise e

    def get_all(self) -> List[Todo]:
        self.cursor.execute("SELECT * FROM Todos;")
        todos = self.cursor.fetchall()

        for todo in todos:
            print(todo)

        return []


class FirebaseTodoRepository(TodoPort):
    pass