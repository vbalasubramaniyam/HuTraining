import pytest

from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Pages.TaskPage import TaskPage
from Main_API_Assignment.Pages import User
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil

class Test_VerifyTask:
    def test_getTask(self,getData):
       token=test_getToken.test_token(getData)
       headers = {'Authorization': token, "Content-Type": "application/json"}
       url='https://api-nodejs-todolist.herokuapp.com/task'
       details=[]
       details= User.getAllTask(url, headers, expectedstatuscode=200)
       Task=TaskPage()
       for x in details:
           Task.verifyAllTask(x,getData["task"])




    @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
    def getData(self,request):
     return request.param