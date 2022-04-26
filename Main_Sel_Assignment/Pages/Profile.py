import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    myAddress = (By.XPATH, "//*[text()='Manage Addresses']")
    AddAddress=(By.XPATH,"//*[text()='ADD ADDRESSES']")
    name=(By.XPATH,"//*[@name='name']")
    phone=(By.NAME,"phone")
    pincode=(By.NAME,"pincode")
    locality=(By.NAME,"addressLine2")
    address=(By.NAME,"addressLine1")
    city=(By.NAME,"city")
    state=(By.NAME,"state")
    homeRadioButton=(By.XPATH,"//*[text()='Home']")
    saveButton=(By.XPATH,"//*[text()='Save']")

    # Select State from DropDown
    def selectState(self,fstate):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(*ProfilePage.state))
        # select by select_by_visible_text() method
        sel.select_by_visible_text(fstate)
        time.sleep(0.8)
        return self
    # Verify whether the Address is Saved
    def verifyAddressSaved(self, value):
        self.driver.implicitly_wait(10)  # seconds
        element = self.driver.find_element(By.XPATH, "//*[text()=\"" + value + "\"]")
        return element

    # Add Address
    def addAddress(self,fname,fphone,fpincode,flocality,faddress,fcity,fstate):
        try:
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.myAddress).click()
            self.driver.find_element(*ProfilePage.AddAddress).click()
            self.driver.find_element(*ProfilePage.name).send_keys(fname)
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.phone).send_keys(fphone)
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.pincode).send_keys(fpincode)
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.locality).send_keys(flocality)
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.address).send_keys(faddress)
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.homeRadioButton).click()
            self.driver.implicitly_wait(20)  # seconds
            self.driver.find_element(*ProfilePage.saveButton).click()
        except Exception:
            raise Exception.with_traceback()