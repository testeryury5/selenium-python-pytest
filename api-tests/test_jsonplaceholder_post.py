import requests
import pytest


@pytest.mark.apitest
def test_create_post():
    payload = {
        'title': 'Group ITSIM 1024',
        'body': 'I love learning automation! It is so exciting!',
        'userId': 101,
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)
    response.status_code == 201
    json_data = response.json()

