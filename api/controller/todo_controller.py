from fastapi import APIRouter

from model.todo_model import TodoModel
from service.todo_service import TodoService
from api.request.todo_create_request import TodoCreateRequest
from api.request.todo_update_request import TodoUpdateRequest
from api.response.todos_response import TodosResponse

router = APIRouter()
todo_service = TodoService()


@router.get("/todos", status_code=200, response_model=TodosResponse, description="TODOリストを取得")
async def get_todos() -> list[TodoModel]:
    """
    TODOリストを取得する
    """
    return TodosResponse(
        todos=todo_service.get_todos()
    )


@router.post("/todos", status_code=201, description="TODOを作成")
async def create_todo(request_body: TodoCreateRequest) -> None:
    """
    TODOを作成する
    """
    todo_service.create_todo(request_body)


@router.put("/todos/{todo_id}", status_code=200, description="TODOを更新")
async def update_todo(todo_id: int, request_body: TodoUpdateRequest) -> None:
    """
    TODOを更新する
    """
    todo_service.update_todo(todo_id, request_body)


@router.delete("/todos/{todo_id}", status_code=200, description="TODOを削除")
async def delete_todo(todo_id: int) -> None:
    """
    TODOを削除する
    """
    todo_service.delete_todo(todo_id)
