import requests
import pytest


@pytest.mark.apitest
def test_get_character_by_id():
    response = requests.get("https://rickandmortyapi.com/api/character/2")
    assert response.status_code == 200

