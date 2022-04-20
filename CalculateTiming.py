import CSVReader


class CalculateTiming():
    def solve(self, s, n):
        h, m = map(int, s[:-2].split(':'))
        h %= 12
        if s[-2:] == 'pm':
            h += 12
        t = h * 60 + m + n
        h, m = divmod(t, 60)
        h %= 24
        suffix = 'a' if h < 12 else 'p'
        h %= 12
        if h == 0:
            h = 12
        return "{:02d}:{:02d}{}m".format(h, m, suffix)

    def getData(self, movie):
        no_of_shows = CSVReader.NoOfShows(movie)
        length = CSVReader.getLengthOfmovie(movie)
        firstShow = CSVReader.getFirstShow(movie)

        time = length.split(" ")

        a = int(time[0]) + 1;
        totalMoviewithInterval = a * 60

        print(firstShow)
        loopshow = int(no_of_shows) - 1
        for i in range(int(loopshow)):
            firstShow = self.solve(firstShow, totalMoviewithInterval)
            print(firstShow)


