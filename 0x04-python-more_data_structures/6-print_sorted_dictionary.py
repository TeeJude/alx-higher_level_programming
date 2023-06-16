#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_sort = list(a_dictionary.keys())
    list_sort.sort()
    for k in list_sort:
        print("{}: {}".format(k, a_dictionary.get(k)))
