import json

import pytest

from fastweather.db import crud
from fastweather.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


def test_post_task(client, monkeypatch):

    expected = {
        "request_id": "1",
        "created_at": "2020-12-05T13:18:32.222557",
        "status": "PENDING",
        "percentage_completed": "0%",
        "data": [],
    }

    async def mock_add_crud(data):
        return expected

    monkeypatch.setattr(crud, "add_weather_request", mock_add_crud)

    response = client.post("/tasks", json={"request_id": 1})
    assert response.status_code == 202

    for k, value in response.json().items():
        if k == "created_at":
            continue
        assert value == expected[k]


def test_get_task_success(client):
    response = client.get("/tasks/1")
    assert response.status_code == 200

    expected = {
        "request_id": "1",
        "status": "COMPLETE",
        "percentage_completed": "100.0%",
    }

    for k, value in response.json().items():
        if k in ["created_at", "data"]:
            continue
        assert value == expected[k]

    assert len(response.json()["data"]) >= 1


def test_get_task_failure(client):
    response = client.get("/tasks/5")
    assert response.status_code == 404
