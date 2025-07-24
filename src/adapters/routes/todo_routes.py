import httpx
import json
from fastapi import APIRouter, Response

from src.core.domain.todo import Todo
from src.core.services.todo_service import TodoService
from src.adapters.repositories.todo_repository import PostgresTodoRepository

todos = APIRouter()
repository = PostgresTodoRepository()
service = TodoService(repository)

@todos.get("/todo")
def get_all():
    todos = service.get_all()

    return Response(
        content=json.dumps(
            {
                "todos": todos,
                "count": len(todos),
                "message": "Todos obtenidos satisfactoriamente!"
            }
        ),
        status_code=httpx.codes.OK
    )

@todos.post("/todo")
def create(new_todo: Todo):
    message = service.create(new_todo)

    return Response(
        content=json.dumps(
            {
                "message": message
            }
        ),
        status_code=httpx.codes.CREATED
    )
