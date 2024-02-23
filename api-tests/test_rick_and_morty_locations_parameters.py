import requests
import pytest


@pytest.mark.apitest
def test_get_locations_with_parameter():
    response = requests.get("https://rickandmortyapi.com/api/location", params={"name":"Earth"})
    assert response.status_code == 200
    json_data = response.json()
    assert 'Earth' in json_data['results'][0]['name']