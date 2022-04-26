from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil
from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil
import pytest


class Test_Filter(BaseClass):


    def test_filteritem(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
         # table=ExcelUtil.getTestData['TestCase1']
        log.info("User name is " + getData["Username"])
        homePage.login_flipkart(getData["Username"],getData["Password"])
        log.info("Logged in successfully")
        product=homePage.gotoProduct()
        product.verifysearchandfilter()


    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self, request):
        return request.param