#!/usr/bin/python3
"""Defines a class named Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student.

        If attrs is a list of strings, retrieve only those attributes
        included in the list or else retrieve all attributes

        Args:
            attrs (list): (Optional) Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(name) == str for name in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.

        Args:
            json (dict): Key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
