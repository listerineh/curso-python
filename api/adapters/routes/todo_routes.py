import httpx
import json
from fastapi import APIRouter, Response

from api.adapters.dtos.todo_dtos import TodoDeleteRequest, TodoPostRequest, TodoPutRequest
from api.core.domain.todo import Todo
from api.core.services.todo_service import TodoService
from api.adapters.repositories.todo_repository import PostgresTodoRepository, InMemoryTodoRepository

todos = APIRouter()
repository = InMemoryTodoRepository()
service = TodoService(repository)

@todos.get("/todo")
def get_all_todos():
    try:
        todos = service.get_all()
    except Exception as e:
        raise e

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
def create_todo(new_todo: TodoPostRequest):
    message = service.create(new_todo.parse())

    return Response(
        content=json.dumps(
            {
                "message": message
            }
        ),
        status_code=httpx.codes.CREATED
    )

@todos.put("/todo")
def update_todo(new_data: TodoPutRequest):
    id, todo = new_data.parse()
    message = service.update(id, todo)

    return Response(
        content=json.dumps(
            {
                "message": message
            }
        ),
        status_code=httpx.codes.ACCEPTED
    )

@todos.delete("/todo")
def delete_todo(new_data: TodoDeleteRequest):
    message = service.delete(new_data.id)

    return Response(
        content=json.dumps(
            {
                "message": message
            }
        ),
        status_code=httpx.codes.OK
    )