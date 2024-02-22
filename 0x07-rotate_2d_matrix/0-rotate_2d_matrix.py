#!/usr/bin/python3
"""rotate_2d_matrix method"""

def rotate_2d_matrix(matrix):
    """rotate 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
