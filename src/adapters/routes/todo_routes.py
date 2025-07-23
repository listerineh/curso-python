from fastapi import APIRouter

from src.core.domain.todo import Todo
from src.core.services.todo_service import TodoService
from src.adapters.repositories.todo_repository import InMemoryTodoRepository

todos = APIRouter()
repository = InMemoryTodoRepository()
service = TodoService(repository)

@todos.get("/todo")
def get_all():
    todos = service.get_all()

    return {
        "todos": todos,
        "count": len(todos),
        "message": "Todos obtenidos satisfactoriamente!"
    }

@todos.post("/todo")
def create(new_todo: Todo):
    message = service.create(new_todo)

    return {
        "todo": new_todo,
        "message": message
    }