from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def __init__(self, driver):
    """ This function is called every time a new object of the base class is created"""
    self.driver = driver


def click(self, by_locator):
    """ Performs click on web element whose locator is passed to it"""
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()


def enter_text(self, by_locator, text):
    """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
    return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


def get_title(self, title) -> str:
    """Returns the title of the page"""
    WebDriverWait(self.driver, 10).until(EC.title_is(title))
    return self.driver.title

