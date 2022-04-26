import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    searchProduct = (By.XPATH, "//*[@name='q']")
    searchicon = (By.XPATH, "//*[@type='submit'']")
    groceryDept=(By.XPATH,"//*[@alt='Grocery']")
    pincode=(By.XPATH,"//*[@name='pincode']")
    firstonerupeeitem=(By.XPATH,"(//*[text()='₹1']/following::button[1])[1]")
    secondonerupeeitem = (By.XPATH, "(//*[text()='₹1']/following::button[1])[1]")
    searchbox = (By.XPATH, "//input[@title='Search for products, brands and more']")
    filterby = (By.XPATH, "//div[text()='Tata']")
    listfilter = (By.XPATH, "//a[contains(text(),'Tata')]")

    def verifysearchandfilter(self):
        self.driver.find_element(*ProductPage.searchbox).send_keys("Besan", Keys.ENTER)
        time.sleep(3)
        besandisplayed = self.driver.find_element(*ProductPage.filterby)
        print(besandisplayed.is_displayed())
        besandisplayed.click()

        listofbasan = self.driver.find_elements(*ProductPage.listfilter)
        for i in listofbasan:
            assert ("Tata" in i.text)
            print(i.text)

        return self

    def searchProduct_Flipkart(self,item):
         self.driver.implicitly_wait(10)  # seconds
         self.driver.find_element(*ProductPage.searchProduct).send_keys(item)
         self.driver.find_element(*ProductPage.searchicon).click()
         return self
    def addtoCart(self,value):
        self.driver.implicitly_wait(10)  # seconds
        self.driver.find_element(By.XPATH,"(//*[text()='"+value+"'])[2]//following::button[2]")
    def clickGrocery(self):
        self.driver.implicitly_wait(10)  # seconds
        return self.driver.find_element(*ProductPage.groceryDept).click()

    def enterPincode(self,pincode):
         self.driver.find_element(*ProductPage.pincode).send_keys(pincode)