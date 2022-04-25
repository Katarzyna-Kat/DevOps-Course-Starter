import os
import requests
from todo_app import app
from unittest.mock import Mock
from dotenv import load_dotenv, find_dotenv

import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app.app import create_app


@pytest.fixture
def client():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    with create_app().test_client() as client:
        yield client


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, "get", get_lists_stub)
    response = client.get("/")

    assert response.status_code == 200
    assert b"Test card" in response.data


class StubResponse:
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def get_lists_stub(url, headers):
    test_board_id = os.environ.get("BOARD_ID")
    fake_response_data = []
    if url.startswith(f"https://api.trello.com/1/boards/{test_board_id}/lists"):
        fake_response_data = [
            {
                "id": "123abc",
                "name": "To Do",
                "cards": [{"id": "456", "name": "Test card"}],
            }
        ]
        return StubResponse(fake_response_data)
    raise Exception
