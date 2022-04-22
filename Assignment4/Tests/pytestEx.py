import pytest
from selenium import webdriver


class pytestEx():

    def test_Weather1(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://weathershopper.pythonanywhere.com/")
        self.driver.maximize_window()


