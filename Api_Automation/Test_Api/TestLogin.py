import json

import requests


def test_login():
    headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjUxMjE0MDgwLCJqdGkiOiJjYTdhYWMzZC0zODdiLTQ5MTMtYmY3NC04MGUzNmI0NjQwYmUiLCJuYmYiOjE2NTEyMTQwODAsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiI2MjZiODUzZGViODY2MmI5NmEzMTdlMjYiLCJleHAiOjE2NTEyMTQ5ODB9.5KXo8sP1NR_02nLgWOV1ckCZ-q5d_PPCh4fZUn6ALdY"}

    response=requests.get("https://hbs-ob-stage.herokuapp.com/protected_test",headers=headers)
    print(response.json())
    assert response.status_code==200

