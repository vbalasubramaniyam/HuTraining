
import pytest

from Main_API_Assignment.Utility import Util
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil


def test_Login(getData):
  endpoint="login"

  payload = {
      "email": getData["email"],
      "password": getData["Password"],
  }
  token=Util.post(endpoint,payload,headers=None,expectedstatuscode=200)
  logoutendpoint="logout"
  originalToken=token["token"]
  token1='Bearer '+originalToken
  headers = {'Authorization': token1 }
  Util.post(logoutendpoint, payload=None, headers=headers, expectedstatuscode=200)

@pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
def getData(request):
    return request.param