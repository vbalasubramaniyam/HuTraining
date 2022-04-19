import csv
import pandas as pd

from UserRegistration import UserRegistration


class Login():
    Title = ""
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"

    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
            self.welcomeAdmin()

        else:
            print(self.error)

    def addnewmovie(Self,Title, Cast, Director, Gen, Length, AdminRating, Lang):

        with open('MovieDb.csv', 'w', newline='') as file:

            fieldnames = ['Title', 'Cast', 'Director', 'Genre', 'Length', 'Admin_Rating', 'Lang','Timing',
                          'No_Of_Shows', 'FirstShow', 'Int_time', 'Gap_Bw_Shows', 'Capacity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Title': Title, 'Cast': Cast, 'Director': Director, 'Genre': Gen, 'Length': Length,
                             'Admin_Rating': AdminRating, 'Lang': Lang, 'No_Of_Shows': '5',
                             'FirstShow': '8:00 AM', 'Int_time':'15min','Gap_Bw_Shows': '30 min', 'Capacity': 50})


    def updatemovieDetails(self,item, changedValue):
        # reading the csv file
        df = pd.read_csv("MovieDb.csv")

        if item == 1:
            df.loc[0, 'Title'] = changedValue
        elif item == 2:
            df.loc[0, 'Cast'] = changedValue
        elif item == 3:
            df.loc[0, 'Director'] = changedValue
        elif item == 4:
            df.loc[0, 'Genre'] = changedValue
        elif item == 5:
            df.loc[0, 'Length'] = changedValue
        elif item == 6:
            df.loc[0, 'Admin_Rating'] = changedValue
        else:
            print("Enter valid details")
        # writing into the file
        df.to_csv("MovieDb.csv", index=False)
    def welcomeAdmin(self):
        print('******Welcome Admin*******')
        print('1. Add New Movie Info')
        print('2. Edit Movie Info')
        print('3. Delete Movies')
        print('4.Logout')
        adminInput=int(input("choose your option: "))
        if adminInput == 1:
            Title = input("Enter Title :")
            Cast = input("Enter Cast :")
            dir = input("Enter Director :")
            Gen=input("Enter Genre :")
            Len=input("Enter Length :")
            Admin_Rating=input("Enter Admin Rating :")
            Lang=input("Enter Lang :")
            print('****Timing****')

            self.addnewmovie(Title,Cast,dir,Gen,Len,Admin_Rating,Lang)
            self.welcomeAdmin()
        elif adminInput == 2:
            print('******Welcome Admin*******')
            print('Select movie which you want to edit:')
            mydata = pd.read_csv("MovieDb.csv")
            print(mydata.Title)
            Edit=int(input("Please Select the Item to change: 1.Title,2.Cast,3.Director,4.Genre,5.Length,6.AdminRating :"))
            changeValue=input("Please Enter the Change Value :")
            self.updatemovieDetails(Edit, changeValue)
            print("Value is changed")
            self.welcomeAdmin()
        elif adminInput == 3:
            updatedlist = []
            with open("MovieDb.csv", newline="") as f:
                reader = csv.reader(f)
                print('******Welcome Admin*******')
                movie = input("Title of the movie to be deleted: :")

                for row in reader:  # for every row in the file
                    if row[0] != movie:
                        updatedlist.append(row)
                print(updatedlist)
                with open("MovieDb.csv", "w", newline="") as f:
                    Writer = csv.writer(f)
                    Writer.writerows(updatedlist)
                    print("File has been updated")

                self.welcomeAdmin()
        elif adminInput == 4:
            print("******Welcome to BookMyShow******")
            print("1. Login")
            print("2. Register new account")
            print("3. Exit")
            register =int(input("Enter option :"))
            if register == 2:

                 user=UserRegistration('john doe','user1234','johndoe@gmail.com','1234567891','44')
                 user.registerNewAcc()
                 print('******Welcome to BooyMyShow******')
                 username=input("Enter username :")
                 password=input("Enter password :")
                 user.check(username,password)



log = Login("admin", "admin")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")
log.check()
