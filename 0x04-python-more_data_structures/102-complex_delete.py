#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_val = a_dictionary.copy()
    for i, j, in temp_val.items():
        if value == j:
            a_dictionary.pop(i)
        return (a_dictionary)
