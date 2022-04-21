class BasePage(object):

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver