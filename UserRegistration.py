import pandas as pd
class UserRegistration():


    def __init__(self, name, password,email,phone,age):

        self.name = name
        self.password = password
        self.email=email
        self.phone=phone
        self.age=age
        self.error = "Enter a valid username and password"

    def registerNewAcc(self):
            print('**** Create new Account *****')
            print('Name :',self.name)
            print('Email :',self.email)
            print('Phone :',self.phone)
            print('Age :',self.age)
            print('Password',self.password)
    def check(self,log_id,log_pass):
        if (self.name == log_id and self.password == log_pass):
            print("******Welcome User1******")
            mydata = pd.read_csv("MovieDb.csv")
            print(mydata.Title)
        else:
            print(self.error)

#user=UserRegistration('john doe','user1234','johndoe@gmail.com','1234567891','44')
