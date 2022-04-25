from selenium.webdriver.common.by import By


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
    homeRadioButton=(By.ID,"HOME")
    saveButton=(By.XPATH,"//*[text()='Save']")

    def addAddress(self,fname,fphone,fpincode,flocality,faddress,fcity):
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
        self.driver.find_element(*ProfilePage.city).send_keys(fcity)