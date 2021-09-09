import copy
from typing import Optional
from fastapi import HTTPException

from model.todo_model import TodoModel


class TodoRepository:
    todos: list[TodoModel] = []

    def insert(self, todo: TodoModel) -> int:
        """
        TODOを作成する
        """
        # IDを自動採番
        if self.todos == []:
            todo.id = 0
        else:
            max_id: int = max([todo.id for todo in self.todos])
            todo.id = max_id + 1
        self.todos.append(copy.deepcopy(todo))

        return todo.id

    def update(self, todo: TodoModel) -> None:
        """
        TODOを更新する
        """
        todo_index = self.__get_todo_index(todo.id)
        if todo_index is not None:
            self.todos[todo_index] = copy.deepcopy(todo)
        else:
            raise HTTPException(status_code=404, detail='TODO is not found.')

    def delete_by_id(self, todo_id: int) -> None:
        """
        TODOを削除する
        """
        todo_index = self.__get_todo_index(todo_id)
        if todo_index is not None:
            self.todos.pop(todo_index)
        else:
            raise HTTPException(status_code=404, detail='TODO is not found.')

    def select_by_id(self, todo_id: int) -> TodoModel:
        """
        IDからTODOを取得する
        """
        todo_index = self.__get_todo_index(todo_id)
        if todo_index is not None:
            return self.todos[todo_index]
        else:
            raise HTTPException(status_code=404, detail='TODO is not found.')

    def select_all(self) -> list[TodoModel]:
        """
        TODOを全件取得する
        """
        return self.todos

    def delete_all(self) -> None:
        """
        TODOを全て削除
        """
        self.todos = []

    def __get_todo_index(self, todo_id: int) -> Optional[int]:
        todo_id_list: list[int] = [todo.id for todo in self.todos]
        return todo_id_list.index(todo_id) if todo_id in todo_id_list else None
