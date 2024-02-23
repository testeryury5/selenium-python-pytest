import requests
import pytest


@pytest.mark.apitest
def test_create_todo():
    payload = {
            "userId": 1,
            "title": "SDET job is $50 per hour",
            "completed": False
    }

    head = {
        'User-Agent': 'PostmanRuntime/7.36.3'
    }

    response = requests.post("https://jsonplaceholder.typicode.com/todos", data=payload, headers=head)
    assert response.status_code == 201
    json_data = response.json()
    print(json_data)
    print(response.headers)