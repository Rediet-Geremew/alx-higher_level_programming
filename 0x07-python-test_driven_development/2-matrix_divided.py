#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number (div) and returns a new matrix.
    Each element is rounded to 2 decimal places.
    Parameters:
    matrix (list of lists): A matrix (list of lists of integers or floats).
    div (int or float): The divisor, which must be a number.
    Returns:
    list of lists: The new matrix with elements divided by div.
    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               or if rows are not of the same size,
               or if div is not a number.
    ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) > 0 and not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
