
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCase4():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://webdriveruniversity.com/')

        # self.home_page = WebDriverUniversity(self.driver)

    def AutoText(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="autocomplete-textfield"]').click()
            # prints parent window title
            print("Parent window title: " + self.driver.title)
            # get current window handle
            p = self.driver.current_window_handle
            # get first child window
            chwd = self.driver.window_handles
            for w in chwd:
                # switch focus to child window
                if (w != p):
                    self.driver.switch_to.window(w)
                    break
            time.sleep(0.9)
            textBox=self.driver.find_element(By.XPATH, '//*[@id="myInput"]')
            textBox.send_keys('ho')
            self.driver.find_element(By.XPATH,'//*[@id="myInputautocomplete-list"]').click()
            textBox = self.driver.find_element(By.XPATH, '//*[@id="myInput"]')
            originalText=textBox.get_attribute('value')
            print("original text :"+originalText)
            if(originalText=='Honey'):
                print('Selected text ')
            else:
                print('not selected')
            time.sleep(0.9)

        except:
            print("An exception occurred")
        finally:
            self.driver.quit()


start = TestCase4()
start.AutoText()