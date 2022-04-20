import csv

movies = []


def writeData(moviedata):
    movies.append(moviedata)
    with open('MovieDb.csv', mode='w') as movie_file:
        booking_writer = csv.writer(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(0, len(movies)):
            booking_writer.writerow(movies[i])

        print("Movies added succesfully")


def readData(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row
            l = l + 1
        if l == len(list(csv_reader)):
            print("Movie does not exist")
            return 0


def displaymovies():
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        listval = ''
        for iteration, row in enumerate(csv_reader):
            # listval=row[0]
            print(str(iteration + 1) + " :" + row[0])


def returnmovies():
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dict_val = ''
        listval = ''
        case_list = {}
        for iteration, row in enumerate(csv_reader):
            listval = row[0]
            if iteration in case_list:
                case_list[iteration].append(row[0])
            else:
                case_list[iteration] = [row[0]]
            # print(str(iteration+1)+" :" + row[0])
            dict_val = {iteration: row[0]}
        return case_list


def readalldata():
    li = []
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            li.append(row)

    return li


def readmovieindex(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return l

            else:
                l = l + 1


def readmovies(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row

            else:
                l = l + 1


def getLengthOfmovie(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row[2]

            else:
                l = l + 1


def NoOfShows(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row[7]

            else:
                l = l + 1


def getFirstShow(moviename):
    with open('MovieDb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l = 0
        for row in csv_reader:
            if str(row[0]) == moviename:
                return row[8]

            else:
                l = l + 1


def updatecsv(moviedata, index):
    li = readalldata()
    li[index] = moviedata
    with open('MovieDb.csv', mode='w') as moviefile:
        booking_writer = csv.writer(moviefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        booking_writer.writerows(li)
