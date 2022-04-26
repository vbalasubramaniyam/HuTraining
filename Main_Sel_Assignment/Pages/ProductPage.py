import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage:

    def __init__(self, driver):
        self.driver = driver


    searchbox = (By.XPATH, "//input[@title='Search for products, brands and more']")
    filterby = (By.XPATH, "//div[text()='Tata']")
    listfilter = (By.XPATH, "//a[contains(text(),'Tata')]")

    # Verify the product Based on the search and filter
    def verifysearchandfilter(self):
        self.driver.find_element(*ProductPage.searchbox).send_keys("Besan", Keys.ENTER)
        time.sleep(3)
        besandisplayed = self.driver.find_element(*ProductPage.filterby)
        print(besandisplayed.is_displayed())
        besandisplayed.click()

        listofbasan = self.driver.find_elements(*ProductPage.listfilter)
        for i in listofbasan:
            assert ("Tata" in i.text)
            print(i.text)

        return self

