
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase1():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://webdriveruniversity.com/')

    # self.home_page = WebDriverUniversity(self.driver)

    def clickButton(self):
      try:
        self.driver.find_element(By.XPATH, '//*[@id="button-clicks"]//h1').click()
        # prints parent window title
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
        # switch focus to child window
          if(w != p):
            self.driver.switch_to.window(w)
            break
        time.sleep(0.9)
        self.driver.find_element(By.CSS_SELECTOR,'#button1').click()
        time.sleep(0.9)
        # alert object creation and switching focus to alert
        a = self.driver.switch_to.alert
        # accept the alert
        a.dismiss()
      except:
          print("An exception occurred")
      finally:
          self.driver.quit()

start = TestCase1()
start.clickButton()
