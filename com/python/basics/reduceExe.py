from functools import reduce


class reduceExe():
    lst={2,3,4,5,6}
    multiply=reduce(lambda a,b:a*b,lst)
    print(multiply)
