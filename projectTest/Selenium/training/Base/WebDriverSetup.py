from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverSetup():
    def setUp(self,driver):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self,driver):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()


def click(self, by_locator):
    """ Performs click on web element whose locator is passed to it"""
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

