#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 500, 'M': 1000}
    num = [rom[x] for x in roman_string] + [0]
    r = 0
    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            r = r + num[i]
        else:
            r = r - num[i]
    return r
