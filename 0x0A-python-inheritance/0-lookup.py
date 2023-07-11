#!/usr/bin/python3
"""Defines an object lookup function."""


def lookup(obj):
	"""Returns a list of available attributes."""
	return (dir(obj))


