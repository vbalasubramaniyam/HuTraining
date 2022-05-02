import pytest

from Main_API_Assignment.Pages import User
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil

class Test_Register:
    def test_register(self,getData):
        endpoint = "register"
        payload = {
                "name": getData["Username"],
                "email": getData["email"],
                "password": getData["Password"],
                "age": 20
        }
        headers = {
                'Content-Type': 'application/json'
            }
        User.post(endpoint, payload, headers, expectedstatuscode=201)

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self,request):
        return request.param