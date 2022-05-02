from Main_API_Assignment.Utility.BaseClass import BaseClass
from Main_API_Assignment.Utility.Request_Utility import request_Util

class test_checkstatus():

   def test_checkstatus(self):
       self.req=request_Util()

       self.req.get('status',"200")