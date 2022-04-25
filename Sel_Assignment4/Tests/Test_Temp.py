import pytest
import time

from Sel_Assignment4.Pages.HomePage import HomePage
from Sel_Assignment4.Pages.Payment import PaymentPage
from Sel_Assignment4.Tests.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        temptext = homePage.gettempnow().text
        #print("Temperature is =" + temptext)
        log.info("Temperature is =" + temptext)
        print(temptext.__contains__('2'))
        temp=temptext.split(" ")
        #print("splited value :"+temp[0])
        if  int(temp[0])< 20:
            prodpage = homePage.clickmoisscreen()
            log.info("user is going to add moisturizer in their cart")
            prodpage.addtocart()
            time.sleep(3)
            prodpage.clickoncartbutton()
            time.sleep(3)
            log.info("user successfully added moisturizer")

        else:
            prodpage = homePage.clicksunscreen()
            log.info("user is going to add Sun Screen in their cart")
            prodpage.addtocart()
            time.sleep(3)
            prodpage.clickoncartbutton()
            time.sleep(3)
            log.info("user successfully added Sunscreen")

        payPage = PaymentPage(self.driver)
        log.info("user in the payment section")
        payPage.clickonpaywithcard()
        time.sleep(3)
        payPage.switchtoiframe()
        payPage.enter_emailid('test@gmail.com')
        log.info("user entered the email address")
        payPage.entercardnumber()
        time.sleep(3)
        log.info("user entered the card details")
        payPage.enterExpiry()
        payPage.enterCVCAndZip()
        payPage.clickSubmit()
        time.sleep(3)
        payPage.switchtoiframe()
        msg=payPage.verifyPaymentSuccess()
       # print('****** '+msg)
        if msg==True:
            log.info("Payment was successful")
        else:
            log.error("Payment failure")

        time.sleep(3)