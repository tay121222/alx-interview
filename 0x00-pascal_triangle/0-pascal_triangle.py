#!/usr/bin/python3
"""Contains function def pascal_triangle(n)"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return list()

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
