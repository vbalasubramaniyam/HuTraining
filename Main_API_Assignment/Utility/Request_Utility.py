import json

import requests


class request_Util():
    def __int__(self):
        self.baseurl="https://api-nodejs-todolist.herokuapp.com/user/register"

    def assert_status_code(self):
        assert self.statuscode == int(
            self.expectedstatuscode), f'Expected status code {self.expectedstatuscode} but Actual status code{self.statuscode}'

    def post(self,endpoint,payload=None, headers=None,expectedstatuscode=200):
        if not headers:
            headers={"Content-Type": "application/json"}
        url=self.baseurl
        rs_api=requests.post(url=url,data=json.dumps(payload),headers=headers)
        self.expectedstatuscode=expectedstatuscode
        self.rs_json=rs_api.json()
        self.assert_status_code()
        print(self.assert_status_code())
        return rs_api.json()

    def get(self,endpoint,expectedstatuscode=200):
            self.baseurl = "https://hbs-ob-stage.herokuapp.com/"
            headers={"Content-Type": "application/json"}

            url = self.baseurl + endpoint
            rs_api = requests.get(url, headers=headers)
            self.expectedstatuscode = expectedstatuscode
            self.rs_json = rs_api.json()
            self.assert_status_code()

            return rs_api.json()





