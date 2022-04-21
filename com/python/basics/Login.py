import csv

import CSVReader
from UserRegistration import UserRegistration


class Login():

    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"

    def check(self, log_id, log_pass):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
            self.welcomeAdmin()

        else:
            print(self.error)

    def movieDetails(self):
        print('******Welcome User1******')
        print('Name :', self.name)
        print('Email :', self.email)
        print('Phone :', self.phone)
        print('Age :', self.age)
        print('Password', self.password)
    def welcomeAdmin(self):
        print('******Welcome Admin*******')
        print('1. Add New Movie Info')
        print('2. Edit Movie Info')
        print('3. Delete Movies')
        print('4.Logout')
        adminInput = int(input("choose your option: "))
        if adminInput == 1:
            print("Add new Movie: ")
            print("----------------------------------------------------")
            movietitle = input("Title: ")
            genre = input("Genre: ")
            length = input("Length: ")
            cast = input("Cast: ")
            director = input("Director: ")
            adminrating = input("Admin Rating: ")
            language = input("Language: ")
            print("Timings:")
            print("----------------------------------------------------")
            shows = int(input("Number of Shows in a day: "))
            firstshow = input("First Show: ")
            intervaltime = input("Interval Time: ")
            gap = input("Gap Between Shows: ")
            capacity = int(input("Capacity: "))

            moviedata = [movietitle, genre, length, cast, director, adminrating,
                         language, shows, firstshow, intervaltime, gap, capacity]

            CSVReader.writeData(moviedata)
            self.welcomeAdmin()
        elif adminInput == 2:
            CSVReader.displaymovies()
            print("Edit Movie: ")
            print("----------------------------------------------------")
            moviename = input("Select movie which you want to edit: ")
            li = CSVReader.readData(moviename)

            movietitle = input("Title: ")
            genre = input("Genre: ")
            length = input("Length: ")
            cast = input("Cast: ")
            director = input("Director: ")
            adminrating = input("Admin Rating: ")
            language = input("Language: ")
            print("Timings:")
            print("----------------------------------------------------")
            shows = int(input("Number of Shows in a day: "))
            firstshow = input("First Show: ")
            intervaltime = input("Interval Time: ")
            gap = input("Gap Between Shows: ")
            capacity = int(input("Capacity: "))

            moviedata = [movietitle, genre, length, cast, director, adminrating,
                         language, shows, firstshow, intervaltime, gap, capacity]

            CSVReader.updatecsv(moviedata, CSVReader.readmovieindex(moviename))
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
            register = int(input("Enter option :"))
            if register == 2:
                print('**** Create new Account *****')
                name = input('Enter username :')
                passw = input('Enter password :')
                email = input('Enter email :')
                phone = input('Enter phone number :')
                age = input('Enter age :')
                user = UserRegistration(name, passw, email, phone, age)
                # user.registerNewAcc()
                print('******Welcome to BooyMyShow******')
                username = input("Enter username :")
                password = input("Enter password :")
                user.check(username, password)
