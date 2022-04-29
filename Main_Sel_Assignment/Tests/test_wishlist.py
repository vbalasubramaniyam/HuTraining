import pytest

from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil


class Test_wishlist(BaseClass):

    def test_AddandVerifyWishlist(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("User name is " + getData["Username"])
        homePage.login_flipkart(getData["Username"], getData["Password"])
        log.info("Logged in successfully")
        self.driver.implicitly_wait(60)  # seconds
        homePage.clickFashionWallet()
        self.driver.implicitly_wait(60)  # seconds
        fashion=homePage.gotoFashion()
        fashion.clickpricelowtoHigh()
        fashion.clickwishlistforwallet()
        fashion.clickTshirtSection()
        fashion.clickpricelowtoHigh()
        fashion.clickTshirtwishlist()
        fashion.clickWhishlist()
        status1=fashion.verifyWishlist(getData["Product2"])
        if status1 == True:
            log.info(getData["Product2"] + "Product added to wishlist in successfully")
        else:
            log.error("product not added to the wishlist")

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase5"))
    def getData(self, request):
        return request.param