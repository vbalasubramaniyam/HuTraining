import pytest

from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Utility import Util
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil


def test_getTask(getData):
   token=test_getToken.test_token(getData)
   headers = {'Authorization': token, "Content-Type": "application/json"}
   url='https://api-nodejs-todolist.herokuapp.com/task'
   details=[]
   details=Util.getAllTask(url,headers,expectedstatuscode=200)
   print(details)
   for x in details:
       Util.verifyAllTask(x,getData["task"])




@pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
def getData(request):
 return request.param