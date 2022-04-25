from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    viewAll = (By.XPATH, "//*[text()='View All']")

    def clickViewAll(self):
        self.driver.implicitly_wait(20)  # seconds
        return self.driver.find_element(*CartPage.viewAll).click()
    def verifyGroceryItemsinCart(self, value):
        self.driver.implicitly_wait(10)  # seconds
        element=self.driver.find_element(By.XPATH, "//*[text()=\""+value+"\"]")
        return element