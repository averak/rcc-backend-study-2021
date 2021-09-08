from fastapi.testclient import TestClient

import main
from test.abstract_IT import Abstract_IT
from test.sample.todo_sample import TodoSample
from repository.todo_repository import TodoRepository
from api.request.todo_create_request import TodoCreateRequest


class TodoController_IT(Abstract_IT):
    test_client: TestClient
    todo_repository = TodoRepository()

    # API PATH
    GET_TODOS_PATH = '/todos'
    CREATE_TODO_PATH = '/todos'

    def setUp(self):
        self.test_client = TestClient(main.app)
        # TODO: rollback

    def test_正_TODOリストを取得(self):
        # setup
        todos = [
            TodoSample.builder().build(),
            TodoSample.builder().build(),
            TodoSample.builder().build(),
        ]
        for todo in todos:
            request_body = TodoCreateRequest(title=todo.title, description=todo.description)
            # setupに別のAPI使うべきではないが、インメモリのため仕方がない
            self.test_client.post(self.CREATE_TODO_PATH, json=request_body.__dict__)

        # test
        response = self.test_client.get(self.GET_TODOS_PATH)
        response_body = response.json()

        # verify
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(todos), len(response_body['todos']))
