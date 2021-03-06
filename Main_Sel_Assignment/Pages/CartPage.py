from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    viewAll = (By.XPATH, "//*[text()='View All']")

    # click View AlL option in the CART
    def clickViewAll(self):
        self.driver.implicitly_wait(60)  # seconds
        return self.driver.find_element(*CartPage.viewAll).click()

    # verify selected Grocery Item is available in the Cart
    def verifyGroceryItemsinCart(self, value):
        self.driver.implicitly_wait(60)  # seconds
        element=self.driver.find_element(By.XPATH, "//*[text()=\""+value+"\"]")
        return element