from unittest.mock import Mock

import pytest as pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from src.app import app
from src.services import user_service


def mock_output(return_value=None):
    return lambda *args, **kwargs: return_value


@pytest.fixture
def client():
    with TestClient(app) as _client:
        yield _client


mock_obj = Mock()

mock_session = Session()


def test_create_user(client, monkeypatch):
    created_user = {
        "hashed_password": "stringnotreallyhashed",
        "is_active": True,
        "email": "string",
        "id": 1
    }
    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output(None))
    monkeypatch.setattr(user_service, "create_user", mock_output(created_user))

    request_body = {
        "email": "string",
        "password": "string"
    }

    response = client.post(
        "/users",
        json=request_body
    )

    assert response.status_code == 201
    assert response.json() == created_user


def test_read_users(client, monkeypatch):
    mock_data = {
        "email": "string",
        "id": 0,
        "is_active": "true",
        "items": []
    }

    expected_response = {'email': 'string', 'id': 0, 'is_active': 'true', 'items': []}

    monkeypatch.setattr("sqlalchemy.orm.Query.all", mock_output(mock_data))

    response = client.get("/users/?skip=0&limit=100")

    assert response.status_code == 200
    assert response.json() == expected_response
