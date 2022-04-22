
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path="chromedriver")
driver.set_window_size(1920, 1080)
driver.maximize_window()
alert = Alert(driver)
driver.get("http://webdriveruniversity.com/File-Upload/index.html")
driver.find_element(by=By.XPATH, value="//input[@id='myFile']").send_keys("/Users/vinoth/Documents/GitRepo/Training/Mini assignment 2 - actions.docx")
driver.find_element(by=By.XPATH, value="//input[@id='submit-button']").click()
alert.accept()
time.sleep(5)
driver.quit()

