import CSVReader
from CalculateTiming import CalculateTiming


class UserRegistration():

    def __init__(self, name, password, email, phone, age):

        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age
        self.error = "Enter a valid username and password"

    def registerNewAcc(self):
        print('**** Create new Account *****')
        print('Name :', self.name)
        print('Email :', self.email)
        print('Phone :', self.phone)
        print('Age :', self.age)
        print('Password', self.password)

    def check(self, log_id, log_pass):
        if (self.name == log_id and self.password == log_pass):
            print("******Welcome User1******")
            CSVReader.displaymovies()
            self.userOptions()
        else:
            print(self.error)

    def userOptions(self):
        movie = input('Enter MovieName ')
        l = CSVReader.readmovies(movie)
        print("Title :" + l[0])
        print("Genre: " + l[1])
        print("Length: " + l[2])
        print("Cast: " + l[2])
        print("Admin Rating: " + l[4])
        print("Timings: " + l[5])
        print("userRating : " + l[6])
        print('1.Book Tickets')
        print('2.Cancel Tickets')
        print('3.Give User Rating')
        useropt = int(input('Enter user option :'))
        if useropt == 1:
            c=CalculateTiming()
            c.getData(movie)
            timing=input('Enter the timing')
            print('Timing '+timing)
            print('Remaining Seats :'+l[11])
            seats=input('Enter number of seats :')
            print('Thanks for the Booking')