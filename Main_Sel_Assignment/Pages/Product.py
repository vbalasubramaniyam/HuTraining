from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    addproducct = (By.XPATH, "//button[@class='btn btn-primary']")
    addcartbutton = (By.XPATH, "//button[@onclick='goToCart()']")

    def addtocart(self):
        return self.driver.find_element(*ProductPage.addproducct).click()

    def clickoncartbutton(self):
        return self.driver.find_element(*ProductPage.addcartbutton).click()