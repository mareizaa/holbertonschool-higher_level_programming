#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j ** 2)
        copy.append(row)
    return copy
