import json

import requests


def test_getOtp():
    endpoint="https://hbs-ob-stage.herokuapp.com/get_register_otp"
    headers = {"Content-Type": "application/json"}
    #assert response.status_code==200
    payload={
       "phone": "+919995544777"
    }
    response=requests.post(url=endpoint,data=json.dumps(payload),headers=headers)
    print(response.json())
    assert response.status_code==200

