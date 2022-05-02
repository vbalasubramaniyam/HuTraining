import pytest

from Main_API_Assignment.Pages import User
from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil


class Test_VerifyUser:

    def test_verifyUser(self, getData):
        token = test_getToken.test_token(getData)
        headers = {'Authorization': token, "Content-Type": "application/json"}
        User.verifyUser(headers,getData["Username"],getData["email"],expectedstatuscode=200)

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self, request):
        return request.param