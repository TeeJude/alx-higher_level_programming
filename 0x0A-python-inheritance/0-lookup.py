#!/usr/bin/python3
"""Defines an object's attribute lookup function."""


def lookup(obj):
    """Returns a list available attributes and methods of an object."""
    return (dir(obj))
