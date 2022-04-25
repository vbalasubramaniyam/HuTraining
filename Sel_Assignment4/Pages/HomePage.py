from selenium.webdriver.common.by import By

from Sel_Assignment4.Pages.Product import ProductPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    temper = (By.ID, "temperature")
    sunscreen = (By.XPATH, "//button[text()='Buy sunscreens']")
    moisscreen = (By.XPATH, "//button[text()='Buy moisturizers']")
    moistext =  (By.XPATH, "(//p[@class='text-justify'])[1]")
    suntext = (By.XPATH, "(//p[@class='text-justify'])[2]")

    def gettempnow(self):
        return self.driver.find_element(*HomePage.temper)

    def getsuntext(self):
        return self.driver.find_element(*HomePage.suntext)

    def clicksunscreen(self):
        self.driver.find_element(*HomePage.sunscreen).click()
        productPage = ProductPage(self.driver)
        return productPage

    def getmoistext(self):
        return self.driver.find_element(*HomePage.moistext)

    def clickmoisscreen(self):
        self.driver.find_element(*HomePage.moisscreen).click()
        #self.driver.find_element(*HomePage.sunscreen).click()
        productPage = ProductPage(self.driver)
        return productPage


