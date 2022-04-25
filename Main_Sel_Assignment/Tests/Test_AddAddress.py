from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil
import pytest

class Test_AddAddress(BaseClass):


    def test_address(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("User name is " + getData["Username"])
        homePage.login_flipkart(getData["Username"],getData["Password"])
        log.info("Logged in successfully")
        #time.sleep(3)
        #homePage.switchtoiframe()
        self.driver.implicitly_wait(60)  # seconds
        homePage.clickMyAccount()
        log.info("CLicked My Account")
        profileObj=homePage.gotoProfile()
        profileObj.addAddress()

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase3"))
    def getData(self, request):
        return request.param