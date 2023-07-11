#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Implements printing of the class list, sorted in ascending order."""

    def print_sorted(self):
        """Prints a list in ascending sorted order."""
        print(sorted(self))
