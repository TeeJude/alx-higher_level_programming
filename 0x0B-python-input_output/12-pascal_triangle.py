#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle of n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_val = triangles[-1]
        temp_val = [1]
        for i in range(len(tri_val) - 1):
            temp_val.append(tri_val[i] + tri_val[i + 1])
        temp_val.append(1)
        triangles.append(temp_val)
    return triangles
