from model.todo_model import TodoModel
from repository.todo_repository import TodoRepository


class TodoService:
    todo_repository = TodoRepository()

    def get_todos(self) -> list[TodoModel]:
        return self.todo_repository.select_all()
