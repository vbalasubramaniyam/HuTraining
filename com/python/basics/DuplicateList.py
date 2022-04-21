class DuplicateList():
    ll = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
    temp_list = []
    for each_element in ll:
        if each_element not in temp_list:
         temp_list.append(each_element)
    print(temp_list)
