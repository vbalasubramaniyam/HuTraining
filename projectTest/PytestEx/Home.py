from selenium.webdriver.common.by import By

from Locators import Locators


class Home():
    def __init__(self, driver):
        self.driver = driver
        Loc = Locators()
        self.get_weather_info = Loc.CurrentWeather

    def getWeather(self):
        try:
            todayWeather = self.driver.find_element(By.XPATH, (self.get_weather_info).get_attribute('value'))
            print(todayWeather)
        except Exception as e:
            raise
