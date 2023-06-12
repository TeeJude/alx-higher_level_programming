#!/usr/bin/python3

#function to replace an element in a list at a specific position without modifying the original list
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if 0 <= idx < len(my_list):
        temp[idx] = element
        return (temp)
    return(my_list)
