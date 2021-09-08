from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool
