import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Main_Sel_Assignment.Pages.CartPage import CartPage
from Main_Sel_Assignment.Pages.Profile import ProfilePage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    password = (By.XPATH, "//input[@type='password']")
    LoginBtn = (By.XPATH, "(//button[@type='submit'])[2]")
    searchProduct = (By.XPATH, "//*[@name='q']")
    searchicon = (By.XPATH, "//*[@type='submit']")
    groceryDept = (By.XPATH, "//*[@alt='Grocery']")
    pincode = (By.XPATH, "//*[@name='pincode']")
    firstonerupeeitem = (By.XPATH, "(//*[text()='₹1']/following::button[1])[1]")
    secondonerupeeitem = (By.XPATH, "(//*[text()='₹1']/following::button[1])[1]")
    cart = (By.XPATH, "//*[@href='/viewcart?otracker=Cart_Icon_Click']")
    groceryBasket = (By.XPATH, "//*[contains(text(),'Grocery Basket')]")
    myAccount = (By.XPATH, "//*[text()='My Account']")
    myProfile = (By.XPATH, "//*[text()='My Profile']")

    def searchProduct_Flipkart(self, item):
        self.driver.implicitly_wait(60)  # seconds
        self.driver.find_element(*HomePage.searchProduct).clear()
        self.driver.implicitly_wait(60)  # seconds
        self.driver.find_element(*HomePage.searchProduct).send_keys(item)
        self.driver.implicitly_wait(60)  # seconds
        time.sleep(3)
        self.driver.find_element(*HomePage.searchicon).click()
        time.sleep(3)
        self.driver.implicitly_wait(60)  # seconds
        return self

    def addtoCart(self, value):
        try:
            self.driver.implicitly_wait(60)  # seconds
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[text()='" + value + "']/following::button[2]").click()
        except Exception:
            raise Exception

    def clickGrocery(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*HomePage.groceryDept).click()

    def clickGrocery(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*HomePage.groceryDept).click()

    def clickCart(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*HomePage.cart).click()

    def verifyGroceryBasket(self):
        self.driver.implicitly_wait(20)  # seconds
        totalItem = self.driver.find_element(*HomePage.groceryBasket).get_attribute('innerText')
        return totalItem

    # creating object for Cart Page
    def gotoCart(self):
        cartobj = CartPage(self.driver)
        return cartobj

    # creating object for ProfilePage
    def gotoProfile(self):
        profileObj = ProfilePage(self.driver)
        return profileObj

    def clickMyAccount(self):
        try:
            account = self.driver.find_element(*HomePage.myAccount)

            hover = ActionChains(self.driver)
            hover.move_to_element(account).perform()
            # identify sub menu element
            prof = self.driver.find_element(*HomePage.myProfile)
            # hover over element and click
            hover.move_to_element(prof).click().perform()

        except Exception:
            raise Exception.__traceback__

    def switchtoiframe(self):
        self.driver.switch_to.frame(0)

    def enterPincode(self, pincode):
        self.driver.implicitly_wait(20)  # seconds
        # time.sleep(20)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*HomePage.pincode))
        self.driver.find_element(*HomePage.pincode).send_keys(pincode)
        self.driver.find_element(*HomePage.pincode).send_keys(Keys.RETURN)
        self.driver.implicitly_wait(20)  # seconds

    def login_flipkart(self, username, password):
        try:
            usr = self.driver.find_element(*HomePage.username)
            usr.click()
            usr.send_keys(username)
            self.driver.implicitly_wait(10)  # seconds
            pwd = self.driver.find_element(*HomePage.password)
            pwd.send_keys(password)
            self.driver.implicitly_wait(10)  # seconds
            self.driver.find_element(*HomePage.LoginBtn).click()
            time.sleep(3)
        except Exception:
            raise Exception()
        return self
