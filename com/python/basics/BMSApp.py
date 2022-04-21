import sys

from Login import Login
from UserRegistration import UserRegistration


class BMSApp():

    def callingfun(self):
        print("******Welcome to BookMyShow******")
        print("1. Login")
        print("2. Register new account")
        print("3. Exit")
        opt = int(input('Enter option :'))
        if opt == 1:
            log = Login("admin", "admin")
            log_id = input("Enter your user ID: ")
            log_pass = input("Enter password: ")
            log.check(log_id,log_pass)
        elif opt == 2:
            print('**** Create new Account *****')
            name = input('Enter username :')
            passw = input('Enter password :')
            email = input('Enter email :')
            phone = int(input('Enter phone number :'))
            age = int(input('Enter age :'))
            user = UserRegistration(name, passw, email, phone, age)
            # user.registerNewAcc()
            print('******Welcome to BooyMyShow******')
            username = input("Enter username :")
            password = input("Enter password :")
            user.check(username, password)
        else:
            sys.exit("Exit the program")


v=BMSApp()
v.callingfun()