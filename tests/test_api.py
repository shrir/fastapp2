import pytest
import json
from fastapi.testclient import TestClient
from app.api import app


client = TestClient(app)


@pytest.mark.parametrize(
    "input,expected_status,expected_result",
    [
        pytest.param(
            {"name": "X", "number": 101},
            201,
            {"X": 101},
            id="create_successful"
        ),
    ]
)
def test_create_contact(input, expected_status, expected_result):
    response = client.post("/contact", data=json.dumps(input))
    assert response.status_code == expected_status
    assert response.json() == expected_result


def test_get_contact():
    input = {"name": "X", "number": 101}
    response = client.post("/contact", data=json.dumps(input))
    assert response.status_code == 201
    assert response.json() == {"X": 101}
    response = client.get(f"/contact/{input['name']}")
    assert response.status_code == 200
    assert response.json() == {"X": 101}


def test_get_contact_not_found():
    input = {"name": "X", "number": 101}
    response = client.post("/contact", data=json.dumps(input))
    assert response.status_code == 201
    assert response.json() == {"X": 101}
    response = client.get(f"/contact/{input['name']}")
    assert response.status_code == 200
    assert response.json() == {"X": 101}
