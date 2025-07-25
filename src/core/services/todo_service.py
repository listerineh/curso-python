from typing import List

from src.core.domain.todo import Todo
from src.core.ports.todo_port import TodoPort


class TodoService:
    def __init__(self, port: TodoPort) -> None:
        self.port: TodoPort = port

    def get_all(self) -> List[dict]:
        todos = self.port.get_all()
        parsed_todos = [todo.to_dict() for todo in todos]

        return parsed_todos

    def create(self, new_todo: Todo) -> str:
        if self.port.exists(new_todo.id):
            return f"Todo con id: {new_todo.id} ya existe en el sistema"

        created = self.port.create(new_todo)

        if created:
            return "Todo creado satisfactoriamente"
        else:
            return "No se ha podido crear el todo"

    def update(self, id: str, new_data: Todo) -> str:
        if not self.port.exists(id):
            return f"Todo con id: {id} no existe en el sistema"

        updated = self.port.update(id, new_data)

        if updated:
            return "Todo actualizado satisfactoriamente"
        else:
            return "No se ha podido actualizar el todo"

    def delete(self, id: str) -> str:
        if not self.port.exists(id):
            return f"Todo con id: {id} no existe en el sistema"

        deleted = self.port.delete(id)

        if deleted:
            return "Todo removido satisfactoriamente"
        else:
            return "No se ha podido remover el todo"
