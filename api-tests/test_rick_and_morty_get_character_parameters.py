import requests
import pytest


@pytest.mark.apitest
def test_character_with_parameters():
    response = requests.get("https://rickandmortyapi.com/api/character/", params={"name":"rick", "status":"alive"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.headers["Cache-Control"] == "max-age=259200"
    json_data = response.json()
    assert 'Rick' in json_data['results'][0]['name']
    assert json_data['info']['count'] == 29


