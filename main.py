from fastapi import FastAPI

from api.controller import todo_controller

app = FastAPI()


# routing
app.include_router(todo_controller.router, tags=['TODO'])

# Swagger
app.title = 'TODO API'
app.description = 'TODO APIのドキュメント'
app.version = '1.0.0'


@app.get("/", status_code=200)
async def root():
    return 'Hello World'
