import requests
import pytest


@pytest.mark.apitest
def test_partial_update_post():
    payload = {
        'title': 'SDET job is actually more than $50 per hour'
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", data=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data['title'] == payload['title']