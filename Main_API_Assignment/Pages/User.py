import inspect
import logging

import pytest
import requests
import json

import logging


def getLogger() ->logging.Logger:
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger
def assert_status_code(astatuscode,expectedstatuscode,res):
    assert astatuscode == int(
            expectedstatuscode), f'Expected status code {expectedstatuscode} but Actual status code {astatuscode} Response Json :{res.text}'

def post(endpoint ,payload=None, headers=None ,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/user/"
    if not headers:
        headers ={"Content-Type": "application/json"}
    url =url+endpoint
    rs_api =requests.post(url=url ,data=json.dumps(payload) ,headers=headers)
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode,rs_api.status_code,rs_api)
    log.info('POST response '+rs_api.text)
    wjdata = rs_api.json()
    print()
    print(astatuscode)
    return rs_api.json()


def getAllTask(endpoint , headers ,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/task?limit="
    url =url+endpoint
    rs_api =requests.get(endpoint,headers=headers)
    rs_json = rs_api.json()
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode, rs_api.status_code, rs_api)
    log.info("getAllTask API response: " + rs_api.text)
    #print(astatuscode)
    #print(rs_json)
    details = []
    for data in rs_json["data"]:
        output = (data['description'])
        details.append(output)
        #print(details)
    return details



def verifyUser(headers ,username,email,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/user/me"

    rs_api =requests.get(url,headers=headers)
    rs_json = rs_api.json()
    expectedname=rs_api.json()["name"]
    expectedemail=rs_api.json()["email"]
    assert username ==expectedname ,f'Expected name  {expectedname} but Actual name  {username} '
    assert email == expectedemail, f'Expected email  {expectedemail} but Actual name  {email} '
    log.info("Username and password successfully verified")
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode, rs_api.status_code, rs_api)
    return True