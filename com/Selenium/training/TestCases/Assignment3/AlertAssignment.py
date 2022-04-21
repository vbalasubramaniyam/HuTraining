import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
class AlertAssignment():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://the-internet.herokuapp.com/')

    def AlertEx(self):
        try:
            self.driver.find_element(By.LINK_TEXT, 'JavaScript Alerts').click()
            self.driver.find_element(By.XPATH, '//*[text()="Click for JS Prompt"]').click()
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.send_keys('Test')
            time.sleep(2)
            print("printing alert text")
            print(alert.text)
            alert.accept()
            print("alert accepted")
            time.sleep(3)
            textBox = self.driver.find_element(By.XPATH, '//*[@id="result"]')
            originalText = textBox.get_attribute('innerText')
            print("original text :" + originalText)
            test='Test'
            if str.__contains__(originalText, test):
                print('Text Printed ')
            else:
                print('text not printed')

        except TimeoutException:
            print("no alert")


            time.sleep(2)
            print("prompt alert test passed")
            print("Now running confirm alert test")
        finally:
            self.driver.quit()
a=AlertAssignment()
a.AlertEx()