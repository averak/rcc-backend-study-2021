from fastapi.testclient import TestClient

import main
from test.abstract_IT import Abstract_IT
from test.sample.todo_sample import TodoSample
from api.request.todo_create_request import TodoCreateRequest
from api.request.todo_update_request import TodoUpdateRequest
from api.controller.todo_controller import todo_service


class TodoController_IT(Abstract_IT):
    test_client = TestClient(main.app)
    todo_repository = todo_service.todo_repository

    # API PATH
    BASE_PATH = '/todos'
    GET_TODOS_PATH = BASE_PATH
    CREATE_TODO_PATH = BASE_PATH
    UPDATE_TODO_PATH = BASE_PATH + "/%d"
    DELETE_TODO_PATH = BASE_PATH + "/%d"

    def setUp(self):
        self.todo_repository.delete_all()

    def test_正_TODOリストを取得(self):
        # setup
        todos = [
            TodoSample.builder().build(),
            TodoSample.builder().build(),
        ]
        for todo in todos:
            self.todo_repository.insert(todo)

        # test
        response = self.test_client.get(self.GET_TODOS_PATH)
        response_body = response.json()

        # verify
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(todos), len(response_body['todos']))

    def test_正_TODOを作成(self):
        # setup
        todo = TodoSample.builder().build()
        request_body = TodoCreateRequest(title=todo.title, description=todo.description)

        # test
        response = self.test_client.post(self.CREATE_TODO_PATH, json=request_body.__dict__)

        # verify
        self.assertEqual(201, response.status_code)
        created_todo = self.todo_repository.select_all()[0]
        self.assertEqual(created_todo.title, request_body.title)
        self.assertEqual(created_todo.description, request_body.description)

    def test_正_TODOを更新(self):
        # setup
        todo = TodoSample.builder().is_done(False).build()
        self.todo_repository.insert(todo)

        request_body = TodoUpdateRequest(title='new title', description='new description', is_done=True)

        # test
        response = self.test_client.put(self.UPDATE_TODO_PATH % todo.id, json=request_body.__dict__)

        # verify
        self.assertEqual(200, response.status_code)
        updated_todo = self.todo_repository.select_by_id(todo.id)
        self.assertEqual(updated_todo.title, request_body.title)
        self.assertEqual(updated_todo.description, request_body.description)

    def test_正_TODOを削除(self):
        # setup
        todo = TodoSample.builder().is_done(False).build()
        self.todo_repository.insert(todo)

        # test
        response = self.test_client.delete(self.DELETE_TODO_PATH % todo.id)

        # verify
        self.assertEqual(200, response.status_code)
        self.assertEqual([], self.todo_repository.select_all())
