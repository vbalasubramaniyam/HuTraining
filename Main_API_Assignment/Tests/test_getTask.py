import pytest

from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Pages.TaskPage import TaskPage
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil


class Test_GetTask:

   def test_getTask(self,getData):
      token=test_getToken.test_token(getData)
      headers = {'Authorization': token, "Content-Type": "application/json"}
      task=TaskPage()
      task.getTask("2",headers,expectedstatuscode=200)
      task.getTask("5", headers, expectedstatuscode=200)
      task.getTask("10", headers, expectedstatuscode=200)


   @pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
   def getData(self,request):
    return request.param