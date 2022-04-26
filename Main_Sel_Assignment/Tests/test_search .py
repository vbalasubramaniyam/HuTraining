import pytest

from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil


class Test_search(BaseClass):

    def test_search(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("User name is " + getData["Username"])
        homePage.login_flipkart(getData["Username"], getData["Password"])
        log.info("Logged in successfully")
        product = homePage.gotoProduct()
        product.verifysearchandfilter(getData["brand"])

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self, request):
        return request.param
