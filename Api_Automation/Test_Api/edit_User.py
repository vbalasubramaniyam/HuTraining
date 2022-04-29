import json

import requests


def test_editUser():
    endpoint="https://hbs-ob-stage.herokuapp.com/user"
    headers = {"Content-Type": "application/json"}
    payload={
    "name": "user888",
    "phone": "+919995544777",
    "email": "user555@hashedin.com",
    "password": "admin",
    "otp": 111111
     }
    response=requests.put(url=endpoint,data=json.dumps(payload),headers=headers)
    print(response.json())
    assert response.status_code==200