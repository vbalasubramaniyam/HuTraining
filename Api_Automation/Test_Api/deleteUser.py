import json

import requests


def test_deleteUser():
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    headers = {"Content-Type": "application/json"}
    payload={

            "phone": "+919995544777",
            "otp": 111111

    }
    response=requests.delete(url=endpoint,data=json.dumps(payload),headers=headers)
    print(response.json())
    assert response.status_code==200