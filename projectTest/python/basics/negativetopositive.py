class negativetopositive():
    lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]

    lst2 = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, lst1)))
    print(lst2)