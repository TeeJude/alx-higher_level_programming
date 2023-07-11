#!/usr/bin/python3
"""Defines a class named Student."""


class Student:
    """Represents a student."""

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

    def to_json(self):
        """Retrieve a dictionary representation of the Student."""
        return self.__dict__
