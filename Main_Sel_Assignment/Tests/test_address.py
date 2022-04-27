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
        self.driver.implicitly_wait(60)  # seconds
        homePage.clickMyAccount()
        log.info("CLicked My Account")
        profileObj=homePage.gotoProfile()
        profileObj.addAddress(getData["fname"],getData["Username"],getData["Pincode"],getData["flocality"],getData["faddress"])
        element=profileObj.verifyAddressSaved(getData["fname"])
        if element.is_displayed():
            log.info(getData['fname'] + " Address Saved Sucessfully")
        else:
            log.error("Address not saved")
    @pytest.fixture(params=ExcelUtil.getTestData("TestCase4"))
    def getData(self, request):
        return request.param