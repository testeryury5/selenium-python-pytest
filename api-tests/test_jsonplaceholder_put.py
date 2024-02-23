import requests
import pytest


@pytest.mark.apitest
def test_update_post():
    payload = {
        'id': 1,
        'title': 'Automation Group',
        'body': 'We are learning automation',
        'userId': '200',
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=payload)
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert json_data['userId'] == payload['userId']