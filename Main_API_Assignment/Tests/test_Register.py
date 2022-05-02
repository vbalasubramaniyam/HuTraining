import json

import pytest

from Main_API_Assignment.Utility import Util
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil


def test_register(getData):
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
    Util.post(endpoint,payload,headers,expectedstatuscode=201)

@pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
def getData(request):
    return request.param