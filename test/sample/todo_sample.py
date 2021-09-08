from model.todo_model import TodoModel


class TodoSampleBuilder:
    _id = 1
    _title = 'SAMPLE'
    _description = 'SAMPLE'
    _is_done = False

    def id(self, id: int):
        self._id = id
        return self

    def title(self, title: str):
        self._title = title
        return self

    def description(self, description: str):
        self._description = description
        return self

    def is_done(self, is_done: bool):
        self._is_done
        return self

    def build(self) -> TodoModel:
        return TodoModel(id=self._id, title=self._title, description=self._description, is_done=self._is_done)


class TodoSample:
    @staticmethod
    def builder() -> TodoSampleBuilder:
        return TodoSampleBuilder()
