import pytest

from Main_API_Assignment.Utility import Util
from Main_API_Assignment.Utility.BaseClass import BaseClass
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil
import logging

class Test_Login():

    def test_Login(self,getData):
      endpoint="login"

      payload = {
          "email": getData["email"],
          "password": getData["Password"]
      }

      Util.post(endpoint,payload,headers=None,expectedstatuscode=200)

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self,request):
        return request.param