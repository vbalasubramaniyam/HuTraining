import json

import requests


def test_createUser():
    endpoint="https://hbs-ob-stage.herokuapp.com/user"
    headers = {"Content-Type": "application/json"}
    payload={
    "name": "user555",
    "phone": "+919995544777",
    "email": "user555@hashedin.com",
    "password": "admin",
    "otp": 111111
     }
    response=requests.post(url=endpoint,data=json.dumps(payload),headers=headers)
    print(response.json())
    assert response.status_code==201