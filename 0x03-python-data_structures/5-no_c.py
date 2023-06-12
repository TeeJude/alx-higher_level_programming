#!/usr/bin/python3

#function to remove all characters c and C from a string.
def no_c(my_string):
    remove = [x for x in my_string if x != "c" and x != "C"]
    return ("".join(remove))
