#!/usr/bin/python3
"""Defines a function that reads text file."""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to standard output."""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
