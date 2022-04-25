from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    searchProduct = (By.XPATH, "//*[@name='q']")
    searchicon = (By.XPATH, "//*[@type='submit'']")
    groceryDept=(By.XPATH,"//*[@alt='Grocery']")
    pincode=(By.XPATH,"//*[@name='pincode']")
    firstonerupeeitem=(By.XPATH,"(//*[text()='₹1']/following::button[1])[1]")
    secondonerupeeitem = (By.XPATH, "(//*[text()='₹1']/following::button[1])[1]")

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