
import pytest

from Main_API_Assignment.Pages import User
from Main_API_Assignment.Utility.BaseClass import BaseClass
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil

class Test_Login(BaseClass):
    def test_Login(self,getData):
      log=self.getLogger()
      endpoint="login"

      payload = {
          "email": getData["email"],
          "password": getData["Password"],
      }
      token= User.post(endpoint, payload, headers=None, expectedstatuscode=200)
      log.info("Logged in successfully")
      logoutendpoint="logout"
      originalToken=token["token"]
      token1='Bearer '+originalToken
      headers = {'Authorization': token1 }
      User.post(logoutendpoint, payload=None, headers=headers, expectedstatuscode=200)
      log.info("logout in successfully")
    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self,request):
        return request.param