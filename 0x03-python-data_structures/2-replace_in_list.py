#!/usr/bin/python3

# function to replace an element of a list at a specific position
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return (my_list)
