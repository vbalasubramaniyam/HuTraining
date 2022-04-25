import pytest
from selenium import webdriver
import time
driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture
def setup(request):
    global driver

    #driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("https://weathershopper.pythonanywhere.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()