#!/usr/bin/python3
"""Defines a class class MyList that inherits from list."""


class MyList(list):
    """Implements printing list class, sorted in ascending order."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))

