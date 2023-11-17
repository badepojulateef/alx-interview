#!/usr/bin/python3
"""
Rotate n x n 2D matrix to 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise.

    Args:
    - matrix (list of lists): The input matrix to be rotated.

    Returns:
    - None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
