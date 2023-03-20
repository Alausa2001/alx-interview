#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    rotate the matrix 90 degrees clockwise.
    """
    n = len(matrix)
    # col = 0
    copy = matrix.copy()

    for idx in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(copy[j][idx])
        matrix[idx] = temp


if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    rotate_2d_matrix(matrix)
    print(matrix)
