from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

    paywithcard = (By.XPATH, "//span[text()='Pay with Card']")
    emailid = (By.XPATH, "//*[@placeholder='Email']")
    cardnumber = (By.XPATH, "//*[@id='card_number']")
    expiry = (By.XPATH, "//*[@id='cc-exp']")
    cvc = (By.XPATH, "//*[@id='cc-csc']")
    zipCode=(By.XPATH, "//*[@id='billing-zip']")
    PaymentSuccessMsg = (By.XPATH, "//*[text()='PAYMENT SUCCESS']")
    submit=(By.XPATH,"//*[@id='submitButton']")


    def clickonpaywithcard(self):
        return self.driver.find_element(*PaymentPage.paywithcard).click()

    def enter_emailid(self,email_id):
       try:
         element= self.driver.find_element(*PaymentPage.emailid)
         element.click()
         element.send_keys(email_id)
       except Exception :
          print(Exception.with_traceback())
       return self
    def entercardnumber(self):
        element=self.driver.find_element(*PaymentPage.cardnumber)
        element.send_keys('4242')
        element.send_keys('4242')
        element.send_keys('4242')
        element.send_keys('4242')
        return self
    def enterCVCAndZip(self):
        cvcCard=self.driver.find_element(*PaymentPage.cvc)
        cvcCard.send_keys('222')
        zipCodeEle=self.driver.find_element(*PaymentPage.zipCode)
        zipCodeEle.send_keys('666666')
        return self
    def enterExpiry(self):
        try:
         expiry=self.driver.find_element(*PaymentPage.expiry)
         expiry.send_keys('02')
         expiry.send_keys('24')
        except Exception:
            print("Exception")
        return self
    def verifyPaymentSuccess(self):
        try:
         #paymentMsg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='PAYMENT SUCCESS']")))
        # paymentMsg= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*PaymentPage.PaymentSuccessMsg))
         paymentMsg =self.driver.find_element(*PaymentPage.PaymentSuccessMsg)
         if paymentMsg.is_displayed():
             return True
        except NoSuchElementException:
             return False

    def clickSubmit(self):
        return self.driver.find_element(*PaymentPage.submit).click()
    def switchtoiframe(self):
        self.driver.switch_to.frame(0)