#!/usr/bin/python3
"""Defines a function that rotates a 2d martrix"""

def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix by 90 degrees"""
    final = []

    for i in range(len(matrix)):
        for j in range(len(matrix)-1, -1, -1):
            final.append(matrix[j][i])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = final.pop(0)
