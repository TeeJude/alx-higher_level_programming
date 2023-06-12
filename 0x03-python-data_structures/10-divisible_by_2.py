#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    division =[]
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            division.append(True)
        else:
            division.append(False)
    return (division)
