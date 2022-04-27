import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class FashionPage:

    def __init__(self, driver):
        self.driver = driver

    pricelowtohigh=(By.XPATH,"//*[text()='Price -- Low to High']")
    wallet=(By.XPATH,"//*[text()='PASSION PETALS']")
    wishlisticon=(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div[1]/div/div[2]")
    mensection=(By.XPATH,"(//*[text()='Men'])[1]")
    tshirt=(By.XPATH,"//*[text()='T-Shirts']")
    yellowtshirt=(By.XPATH,"(//*[text()='Printed Men Round Neck Yellow T-Shirt'])[1]")
    walletwishlist=(By.XPATH,"(//*[@opacity='.9'])[1]")
    #tshirtwishlist=(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a/div[4]")
    wishlisttext=(By.XPATH,"//*[text()='Wishlist']")
    myAccount = (By.XPATH, "//*[text()='My Account']")

    # Verify Wishlist
    def verifyWishlist(self, value):
     try:
         self.driver.implicitly_wait(60)  # seconds
         time.sleep(3)
         element=self.driver.find_element(By.XPATH, "//*[contains(text(),\'"+value+"\')]")
         return True
     except Exception:
        raise False

    # click price low to high
    def clickpricelowtoHigh(self):
        self.driver.implicitly_wait(30)  # seconds
        time.sleep(3)
        return self.driver.find_element(*FashionPage.pricelowtohigh).click()

    # click wishlist icon
    def clickwishlistforwallet(self):
        self.driver.implicitly_wait(60)  # seconds
        time.sleep(3)
        return self.driver.find_element(*FashionPage.walletwishlist).click()

    # click wishlist tshirt icon
    def clickTshirtwishlist(self):
        self.driver.implicitly_wait(60)  # seconds
        time.sleep(3)
        return self.driver.find_element(*FashionPage.walletwishlist).click()

    # Click clickTshirtSection from the top Menu
    def clickTshirtSection(self):
        try:
         time.sleep(3)
         account = self.driver.find_element(*FashionPage.mensection)
         hover = ActionChains(self.driver)
         hover.move_to_element(account).perform()
         # identify sub menu element
         tshirtsec = self.driver.find_element(*FashionPage.tshirt)
         # hover over element and click
         hover.move_to_element(tshirtsec).click().perform()

        except Exception:
             raise Exception.__traceback__

    # Click MyAccount from the top Menu
    def clickWhishlist(self):
        try:
            time.sleep(3)
            account = self.driver.find_element(*FashionPage.myAccount)

            hover = ActionChains(self.driver)
            hover.move_to_element(account).perform()
            # identify sub menu element
            prof = self.driver.find_element(*FashionPage.wishlisttext)
            # hover over element and click
            hover.move_to_element(prof).click().perform()

        except Exception:
            raise Exception.__traceback__