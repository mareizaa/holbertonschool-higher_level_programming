#!/usr/bin/python3
"""
Divide each element of the matrix 
by a given number
returns each position / div
"""


def matrix_divided(matrix, div):
    """Divide each element of the matrix"""
    new = []
    length = len(matrix[0])

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        raw = []
        if len(i) == length:
            for value in i:
                if type(value) is int or type(value) is float:
                    result = value / div
                    raw.append(round(result, 2))
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new.append(raw)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    return new
