#!/usr/bin/python3
"""Defines function that inherits from a class."""


def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to compare the type of object to.
    Returns:
        True if object is an inherited instance of class, a_class.
        Otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
