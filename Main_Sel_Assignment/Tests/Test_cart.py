import time

from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Pages.ProductPage import ProductPage
from Main_Sel_Assignment.Tests.BaseClass import BaseClass
from Main_Sel_Assignment.Utils.ExcelUtil import ExcelUtil
import pytest

class Test_Cart(BaseClass):


    def test_cart(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("User name is " + getData["Username"])
        homePage.login_flipkart(getData["Username"],getData["Password"])
        log.info("Logged in successfully")
        #time.sleep(3)
        #homePage.switchtoiframe()
        self.driver.implicitly_wait(60)  # seconds
        homePage.clickGrocery()
        homePage.enterPincode(getData['Pincode'])
        homePage.searchProduct_Flipkart(getData['Product1'])
        homePage.addtoCart(getData['Product1'])
        homePage.searchProduct_Flipkart(getData['Product2'])
        homePage.addtoCart(getData['Product2'])
        homePage.searchProduct_Flipkart(getData['Product3'])
        homePage.addtoCart(getData['Product3'])
        homePage.clickCart()
        originalValue =homePage.verifyGroceryBasket()
        print("original text :" + originalValue)

        if str.__contains__(originalValue, "3"):
            print('Text Printed ')
            log.info("3 item added in the cart successfully")
        else:
            log.error("Expected item not added in the cart")

        cart=homePage.gotoCart()
        cart.clickViewAll()
        element=cart.verifyGroceryItemsinCart(getData['Product1'])
        if element.is_displayed():
            log.info( getData['Product1']+" item added in the cart successfully")
        else:
            log.error("Expected item not added in the cart")
        element1 = cart.verifyGroceryItemsinCart(getData['product2_dub'])
        if element1.is_displayed():
                log.info(getData['Product2'] + " item added in the cart successfully")
        else:
                log.error("Expected item not added in the cart")
        element2 = cart.verifyGroceryItemsinCart(getData['Product3'])
        if element2.text == getData['Product3']:
            log.info(getData['Product3'] + " item added in the cart successfully")
        else:
            log.error("Expected item not added in the cart")

    @pytest.fixture(params=ExcelUtil.getTestData("TestCase2"))
    def getData(self, request):
        return request.param