import csv

import requests

from Main_API_Assignment.Utility.BaseClass import BaseClass
from Main_API_Assignment.Pages.User import assert_status_code


class TaskPage(BaseClass):

    def __init__(self):
        self.log = self.getLogger()
        self.task=[]

    def verifyAllTask(self,actualvalue, expectedvalue):
        assert actualvalue in expectedvalue
        if str.__contains__(expectedvalue, actualvalue):
            self.log.info(actualvalue + " task is available ")
        else:
            self.log.error(actualvalue + "Task is not available")

    def getTask(self,endpoint, headers, expectedstatuscode=200):

        url = "https://api-nodejs-todolist.herokuapp.com/task?limit="
        url = url + endpoint
        rs_api = requests.get(url, headers=headers)
        rs_json = rs_api.json()
        astatuscode = expectedstatuscode
        assert_status_code(astatuscode, rs_api.status_code, rs_api)
        self.log.info("getTask API response: " + rs_api.text)
        print(astatuscode)
        print(rs_json)
        return rs_api.json()

    def writeData(self,data):

        self.task.append(data)
        with open('Task.csv', mode='w') as movie_file:
            booking_writer = csv.writer(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for i in range(0, len(self.task)):
                booking_writer.writerow(self.task[i])

            print("task added succesfully")