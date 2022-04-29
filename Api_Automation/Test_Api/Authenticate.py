import json

import requests


def test_Authenticate():
    endpoint="https://hbs-ob-stage.herokuapp.com/authenticate"
    headers = {"Content-Type": "application/json"}
    payload={
    "phone": "+919995544777",
    "LoginType": "password",
    "password": "admin"
     }
    response=requests.post(url=endpoint,data=json.dumps(payload),headers=headers)
    print(response.json())
    assert response.status_code==201