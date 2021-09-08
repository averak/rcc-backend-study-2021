from pydantic import BaseModel


class TodoUpdateRequest(BaseModel):
    title: str
    description: str
    is_done: bool
