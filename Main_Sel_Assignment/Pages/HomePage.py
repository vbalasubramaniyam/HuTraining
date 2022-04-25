from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By

from Main_Sel_Assignment.Utils import CSVReader
from Sel_Assignment4.Pages.Product import ProductPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    username = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    password = (By.XPATH, "//input[@type='password']")
    LoginBtn=(By.XPATH,"(//button[@type='submit'])[2]")
    def login_flipkart(self,username,password):
       try:
        # uservalue= CSVReader.getValuefromCSV()
         print(username)
         usr= self.driver.find_element(*HomePage.username)
         usr.click()
         usr.send_keys(username)
         pwd = self.driver.find_element(*HomePage.password)
         pwd.send_keys(password)
         self.driver.find_element(*HomePage.LoginBtn).click()
       except Exception :
          raise Exception()
       return self


