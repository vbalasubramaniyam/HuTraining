import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class TestCase2():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://webdriveruniversity.com/')

    def RadioButtonandCheckBox(self):
            try:
                self.driver.find_element(By.XPATH, '//*[@id="dropdown-checkboxes-radiobuttons"]').click()
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
                time.sleep(3)
                element=self.driver.find_element(By.XPATH, '//*[@id="dropdowm-menu-1"]')
                time.sleep(3)
                sel = Select(element)
                sel.select_by_visible_text('Python')
                checkBox=self.driver.find_element(By.XPATH,'//*[@id="checkboxes"]/label[1]/input')
                checkBox.click()
                time.sleep(3)
                if checkBox.is_selected():
                      print("Check box selected")
                else:
                      print("Checkbox not selected")
                radiobutton = self.driver.find_element(By.XPATH, '//*[@id="radio-buttons"]/input[1]')
                radiobutton.click()
                time.sleep(3)
                if radiobutton.is_selected():
                    print("Radio Button  selected")
                else:
                    print("Radio Button selected")

            except:
                print("An exception occurred")
            finally:
                self.driver.quit()
start = TestCase2()
start.RadioButtonandCheckBox()