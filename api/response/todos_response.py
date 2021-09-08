from pydantic import BaseModel

from model.todo_model import TodoModel


class TodosResponse(BaseModel):
    todos: list[TodoModel]
