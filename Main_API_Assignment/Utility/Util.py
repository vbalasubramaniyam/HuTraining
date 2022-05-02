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
def assert_status_code(astatuscode,expectedstatuscode):
    assert astatuscode == int(
            expectedstatuscode), f'Expected status code {expectedstatuscode} but Actual status code{astatuscode}'

def post(endpoint ,payload=None, headers=None ,expectedstatuscode=200):
    url="https://api-nodejs-todolist.herokuapp.com/user/"
    if not headers:
        headers ={"Content-Type": "application/json"}
    url =url+endpoint
    rs_api =requests.post(url=url ,data=json.dumps(payload) ,headers=headers)
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode,rs_api.status_code)
    wjdata = rs_api.json()
    print()
    print(astatuscode)
    return rs_api.json()

def AddTask(endpoint ,payload=None, headers=None ,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/"
    url =url+endpoint
    rs_api =requests.post(url=url ,data=json.dumps(payload) ,headers=headers)
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode,rs_api.status_code)
    log.info("Add Task API response: " + rs_api.text)
    print(rs_api.text)
    print(astatuscode)
    return rs_api.json()

def getTask(endpoint , headers ,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/task?limit="
    url =url+endpoint
    rs_api =requests.get(url,headers=headers)
    rs_json = rs_api.json()
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode,rs_api.status_code)
    log.info("getTask API response: "+rs_api.text)
    print(astatuscode)
    print(rs_json)
    return rs_api.json()

def getAllTask(endpoint , headers ,expectedstatuscode=200):
    log=getLogger()
    url="https://api-nodejs-todolist.herokuapp.com/task?limit="
    url =url+endpoint
    rs_api =requests.get(endpoint,headers=headers)
    rs_json = rs_api.json()
    astatuscode =expectedstatuscode
    assert_status_code(astatuscode,rs_api.status_code)
    log.info("getAllTask API response: " + rs_api.text)
    #print(astatuscode)
    #print(rs_json)
    details = []
    for data in rs_json["data"]:
        output = (data['description'])
        details.append(output)
        #print(details)
    return details

def verifyAllTask(actualvalue,expectedvalue):
    log = getLogger()
    assert actualvalue in expectedvalue
    if str.__contains__(expectedvalue, actualvalue):
        log.info(actualvalue+" task is available ")
    else:
        log.error(actualvalue +"Task is not available")