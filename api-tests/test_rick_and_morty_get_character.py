import requests
import pytest


@pytest.mark.apitest
def test_get_character():
    response = requests.get("https://rickandmortyapi.com/api/character/2")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = response.json()
    assert json_data['id'] == 2


