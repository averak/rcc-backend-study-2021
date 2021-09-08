from test.abstract_UT import Abstract_UT
from test.sample.todo_sample import TodoSample
from repository.todo_repository import TodoRepository


class TodoRepository_UT(Abstract_UT):
    todo_repository = TodoRepository()

    def setUp(self):
        self.todo_repository.todos = []

    def test_正_TODOを作成する(self):
        # setup
        todo = TodoSample.builder().build()

        # test
        self.todo_repository.insert(todo)

        # verify
        created_todos = self.todo_repository.todos
        self.assertEqual(1, len(created_todos))
        self.assertEqual(todo, created_todos[todo.id])

    def test_正_TODOを更新する(self):
        # setup
        todo = TodoSample.builder().build()
        self.todo_repository.insert(todo)

        # test
        todo.title = 'changed title'
        self.todo_repository.update(todo)

        # verify
        updated_todo = self.todo_repository.todos[todo.id]
        self.assertEqual(todo, updated_todo)

    def test_正_TODOを削除する(self):
        # setup
        todo = TodoSample.builder().build()
        self.todo_repository.insert(todo)

        # test
        self.todo_repository.delete_by_id(todo.id)

        # verify
        self.assertEqual(0, len(self.todo_repository.todos))

    def test_正_IDからTODOを取得(self):
        # setup
        todo = TodoSample.builder().build()
        self.todo_repository.insert(todo)

        # verify
        self.assertEqual(todo, self.todo_repository.select_by_id(todo.id))

    def test_正_TODOを全件取得する(self):
        # setup
        todos = [
            TodoSample.builder().build(),
            TodoSample.builder().build(),
            TodoSample.builder().build(),
        ]
        for todo in todos:
            self.todo_repository.insert(todo)

        # test
        selected_todos = self.todo_repository.select_all()

        # verify
        self.assertEqual(selected_todos, todos)

    def test_正_TODOを全て削除(self):
        # setup
        todos = [
            TodoSample.builder().build(),
            TodoSample.builder().build(),
            TodoSample.builder().build(),
        ]
        for todo in todos:
            self.todo_repository.insert(todo)

        # test
        self.todo_repository.delete_all()

        # verify
        self.assertEqual(0, len(self.todo_repository.todos))
