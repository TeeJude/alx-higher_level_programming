#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    c = 1
    for i in my_list:
        a = a + (i[0] * i[1])
        b = b + i[1]
    c = a/b
    return c
