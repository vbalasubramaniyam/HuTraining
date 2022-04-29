import requests


def test_getrequest():
    response=requests.get("https://hbs-ob-stage.herokuapp.com/status")
    assert response.status_code==200
    