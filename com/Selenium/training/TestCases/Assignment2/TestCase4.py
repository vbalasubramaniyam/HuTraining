
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="chromedriver")
driver.set_window_size(1920, 1080)
driver.get("http://webdriveruniversity.com/Scrolling/index.html")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,2000)","")
target = driver.find_element(by=By.XPATH, value="//div[@id='zone4']")
driver.execute_script('arguments[0].scrollIntoView(true);', target)
time.sleep(3)
target1 = driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")
driver.execute_script('arguments[0].scrollIntoView(true);', target1)
time.sleep(3)
target2 = driver.find_element(by=By.XPATH, value="//h1[@id='zone3-entries']")
driver.execute_script('arguments[0].scrollIntoView(true);', target2)
time.sleep(3)
target3 = driver.find_element(by=By.XPATH, value="//div[@id='zone1']")
driver.execute_script('arguments[0].scrollIntoView(true);', target3)
time.sleep(3)

action = ActionChains(driver)
action.move_to_element(driver.find_element(by=By.XPATH,value="//div[@id='zone1']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone3-entries']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")).move_to_element(driver.find_element(by=By.XPATH, value="//div[@id='zone4']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")).perform()

time.sleep(10)
driver.quit()

