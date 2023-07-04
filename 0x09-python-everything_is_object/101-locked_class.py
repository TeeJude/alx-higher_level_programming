#!/usr/bin/python3
"""Define a class called LockedClass"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance 
    attributes, except if the new instance attribute 
    is called first_name
    """
    __slot__ = ["first_name"]
