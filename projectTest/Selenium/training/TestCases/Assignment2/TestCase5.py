
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="chromedriver")
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/To-Do-List/index.html")
str= "sammmm"
driver.find_element(by=By.XPATH, value="//input[@placeholder='Add new todo']").send_keys(str)
driver.find_element(by=By.XPATH, value="//li[normalize-space()='Go to potion class']").click()
driver.find_element(by=By.XPATH, value="//li[normalize-space()='Buy new robes']").click()


action = ActionChains(driver)
action.move_to_element(driver.find_element(by=By.XPATH, value="//li[normalize-space()='Practice magic']")).move_to_element(driver.find_element(by=By.XPATH, value="//li[normalize-space()='Practice magic']//i[@class='fa fa-trash']")).click().perform()
time.sleep(10)
driver.quit()

