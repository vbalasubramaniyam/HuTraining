import pytest

from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Tests.Test_login import Test_Login
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil


class Test_Logout(BaseClass):

    def test_logout(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # table=ExcelUtil.getTestData['TestCase1']
        log.info("User name is " + getData["Username"])
        status=homePage.login_flipkart(getData["Username"], getData["Password"])
        if status:
            log.info("user logged in successfully")
        else:
            log.error("Please enter valid user details")

        home = HomePage(self.driver)
        home.logout_Flipkart()
        logincheck=home.verifyLogin()
        if logincheck:
            log.info("Logged out successfully")
        else:
            log.error("User not logged out")

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self, request):
        return request.param