import json

import pytest
import requests

from Main_API_Assignment.Tests import test_getToken
from Main_API_Assignment.Utility.ExcelUtil import ExcelUtil
from Main_API_Assignment.Utility.readCSV import read_test_data_from_csv


@pytest.mark.parametrize("Description", read_test_data_from_csv())
def test_Addtask(Description,getData):
  str=Description[0]
  token=test_getToken.test_token(getData)
  headers = {'Authorization': token, "Content-Type": "application/json"}
  payload = {
      "description": str
  }
  response = requests.post("https://api-nodejs-todolist.herokuapp.com/task",data=json.dumps(payload),headers=headers)
  response_body = response.json()
  print(response_body)
  assert response_body["success"] == True


@pytest.fixture(params=ExcelUtil.getTestData("TestCase1"))
def getData(request):
    return request.param