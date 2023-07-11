#!/usr/bin/python3
"""Defines a function that checks and inherited from a class."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an exact instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to compare the type of object to.
    Returns:
        True if object is an exact instance or inherited of class, a_class.
        Otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
