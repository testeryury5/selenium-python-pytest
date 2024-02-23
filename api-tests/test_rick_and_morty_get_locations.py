import requests
import pytest


@pytest.mark.apitest
def test_get_locations():
    response = requests.get("https://rickandmortyapi.com/api/location")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data['info']['count'] == 126
