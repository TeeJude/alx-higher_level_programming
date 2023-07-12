#!/usr/bin/python3
"""Defines a function that inserts a line of text."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given specific in a file.

    Args:
        filename (str): Name of file.
        search_string (str): String to search for within given file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
