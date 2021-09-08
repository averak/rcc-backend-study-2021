import copy

from model.todo_model import TodoModel


class TodoRepository:
    todos: dict[int, TodoModel] = {}

    def insert(self, todo: TodoModel) -> int:
        """
        TODOを作成する
        """
        # IDを自動採番
        todo.id = len(self.todos)
        self.todos[todo.id] = copy.deepcopy(todo)

        return todo.id

    def update(self, todo: TodoModel) -> None:
        """
        TODOを更新する
        """
        if todo.id in self.todos:
            self.todos[todo.id] = copy.deepcopy(todo)

    def delete(self, todo_id: int) -> None:
        """
        TODOを削除する
        """
        if todo_id in self.todos:
            self.todos.pop(todo_id)

    def select_by_id(self, todo_id: int) -> TodoModel:
        """
        IDからTODOを取得する
        """
        if todo_id in self.todos:
            return self.todos[todo_id]
        else:
            return None

    def select_all(self) -> list[TodoModel]:
        """
        TODOを全件取得する
        """
        return list(self.todos.values())

    def delete_all(self) -> None:
        """
        TODOを全て削除
        """
        self.todos = {}
