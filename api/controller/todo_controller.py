from fastapi import APIRouter

from model.todo_model import TodoModel
from service.todo_service import TodoService
from api.response.todos_response import TodosResponse

router = APIRouter()
todo_service = TodoService()


@router.get("/todos/", status_code=200, response_model=TodosResponse)
async def get_todos() -> list[TodoModel]:
    return TodosResponse(
        todos=todo_service.get_todos()
    )
