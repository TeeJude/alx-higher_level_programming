#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function that represents string using JSON."""
import json


def from_json_string(my_str):
    """Return the Python object representation by a JSON string."""
    return json.loads(my_str)
