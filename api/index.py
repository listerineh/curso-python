from fastapi import FastAPI

from api.adapters.routes.todo_routes import todos


app = FastAPI()
app.include_router(todos)


@app.get("/health-check")
def health_check():
    return {
        "status": "Funcionando y saludos desde vercel!"
    }
