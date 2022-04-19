import csv


class Login():
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

            self.addnewmovie(Title,Cast,dir,Gen,Len,Admin_Rating,Lang)
        elif adminInput == 2:
            print("edit movie")
        elif adminInput == 3:
            print("delete movie")
        elif adminInput == 4:
            print("logout")



log = Login("admin", "admin")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")
log.check()