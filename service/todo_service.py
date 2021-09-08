from model.todo_model import TodoModel
from repository.todo_repository import TodoRepository
from api.request.todo_create_request import TodoCreateRequest
from api.request.todo_update_request import TodoUpdateRequest


class TodoService:
    todo_repository = TodoRepository()

    def get_todos(self) -> list[TodoModel]:
        """
        TODOリストを取得する
        """
        return self.todo_repository.select_all()

    def create_todo(self, request_body: TodoCreateRequest) -> None:
        """
        TODOを作成する
        """
        todo = TodoModel(
            id=-1,  # IDを仮で指定する
            title=request_body.title,
            description=request_body.description,
            is_done=False,
        )
        self.todo_repository.insert(todo)

    def update_todo(self, todo_id: int, request_body: TodoUpdateRequest) -> None:
        """
        TODOを更新する
        """
        todo = self.todo_repository.select_by_id(todo_id)
        todo.title = request_body.title
        todo.description = request_body.description
        self.todo_repository.update(todo)

    def delete_todo(self, todo_id: int) -> None:
        """
        TODOを削除する
        """
        self.todo_repository.delete_by_id(todo_id)
