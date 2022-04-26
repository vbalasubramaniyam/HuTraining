from Main_Sel_Assignment.Pages.HomePage import HomePage
from Main_Sel_Assignment.Tests.Test_login import Test_Login


class Test_Logout(Test_Login):

    def test_logout(self,driver):
        log = self.getLogger()
        homePage = HomePage(self.driver)
