import requests


def test_get_response():
    response = requests.get("http://techstepacademy.com")
    assert response.status_code == 200
