import json

import pytest
import requests

from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Utility import Util
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil
from Main_API_Assignment.Utility.readCSV import read_test_data_from_csv



def test_getTask(getData):
   token=test_getToken.test_token(getData)
   headers = {'Authorization': token, "Content-Type": "application/json"}
   Util.getTask("2",headers,expectedstatuscode=200)
   Util.getTask("5", headers, expectedstatuscode=200)
   Util.getTask("10", headers, expectedstatuscode=200)


@pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
def getData(request):
 return request.param