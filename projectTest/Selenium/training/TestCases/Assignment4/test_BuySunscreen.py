import pytest

from projectTest.Selenium.training.Base.BasePage import BasePage
from projectTest.Selenium.training.Pages.WeatherHome import WeatherHome


@pytest.mark.usefixtures('set_up')
class test_BuySunscreen(BasePage):

    def get_Weather(self):
        driver = self.driver
        weather = WeatherHome(driver)
        weather.getWeather()
