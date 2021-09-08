from pydantic import BaseModel


class TodoCreateRequest(BaseModel):
    title: str
    description: str
