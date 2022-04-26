import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Main_Sel_Assignment.Pages.CartPage import CartPage
from Main_Sel_Assignment.Pages.ProductPage import ProductPage
from Main_Sel_Assignment.Pages.Profile import ProfilePage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.error = "Enter a valid username and password"

    username = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    password = (By.XPATH, "//input[@type='password']")
    LoginBtn = (By.XPATH, "(//button[@type='submit'])[2]")
    searchProduct = (By.XPATH, "//*[@name='q']")
    search_Icon = (By.XPATH, "//*[@type='submit']")
    groceryDept = (By.XPATH, "//*[@alt='Grocery']")
    pincode = (By.XPATH, "//*[@name='pincode']")
    cart = (By.XPATH, "//*[@href='/viewcart?otracker=Cart_Icon_Click']")
    groceryBasket = (By.XPATH, "//*[contains(text(),'Grocery Basket')]")
    myAccount = (By.XPATH, "//*[text()='My Account']")
    myProfile = (By.XPATH, "//*[text()='My Profile']")
    logout = (By.XPATH, "//*[text()='Logout']")

    # creating object for Cart Page
    def gotoCart(self):
        cartobj = CartPage(self.driver)
        return cartobj

    # creating object for ProfilePage
    def gotoProfile(self):
        profileObj = ProfilePage(self.driver)
        return profileObj

    # creating object for ProfilePage
    def gotoProduct(self):
        productObj = ProductPage(self.driver)
        return productObj
    # Search a product from Flipkart
    def searchProduct_Flipkart(self, item):
        self.driver.implicitly_wait(60)  # seconds
        self.driver.find_element(*HomePage.searchProduct).clear()
        self.driver.implicitly_wait(60)  # seconds
        self.driver.find_element(*HomePage.searchProduct).send_keys(item)
        self.driver.implicitly_wait(60)  # seconds
        time.sleep(3)
        self.driver.find_element(*HomePage.search_Icon).click()
        time.sleep(3)
        self.driver.implicitly_wait(60)  # seconds
        return self

    # Add Item to the cart
    def addtoCart(self, value):
        try:
            self.driver.implicitly_wait(60)  # seconds
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[text()='" + value + "']/following::button[2]").click()
        except Exception:
            raise Exception

    # click Grocery Icon
    def clickGrocery(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*HomePage.groceryDept).click()

    #click Cart Icon
    def clickCart(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*HomePage.cart).click()
    # Verify the Grocery Basket
    def verifyGroceryBasket(self):
        self.driver.implicitly_wait(20)  # seconds
        totalItem = self.driver.find_element(*HomePage.groceryBasket).get_attribute('innerText')
        return totalItem
    # Click MyAccount from the top Menu
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

    # Logout from the Flipkart Application
    def logout_Flipkart(self):
        try:
            account = self.driver.find_element(*HomePage.myAccount)

            hover = ActionChains(self.driver)
            hover.move_to_element(account).perform()
            # identify sub menu element
            logot = self.driver.find_element(*HomePage.logout)
            # hover over element and click
            hover.move_to_element(logot).click().perform()

        except Exception:
            raise Exception.__traceback__

    # Enter the pincode for Grocery Delivery
    def enterPincode(self, pincode):
        self.driver.implicitly_wait(20)  # seconds
        self.driver.find_element(*HomePage.pincode).send_keys(pincode)
        self.driver.find_element(*HomePage.pincode).send_keys(Keys.RETURN)
        self.driver.implicitly_wait(20)  # seconds

    # Verify User in the Login Page
    def verifyLogin(self):
        try:
            self.driver.implicitly_wait(30)  # seconds
            usr = self.driver.find_element(*HomePage.username)
            if usr.is_displayed():
                return True
            else:
                return False
        except:
            raise Exception

    # Login to Flipkart Application
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
            return True
        except Exception:
            return False

