#!/usr/bin/python3
"""Defines a function that checks a class."""


def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of any given class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to compare the type of object to.
    Returns:
        True if object is an exact instance of class, a_class.
        Otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
