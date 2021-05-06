#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for width in range(len(matrix[i])):
                print("{:d}".format(matrix[i][width]), end="")
                if width != len(matrix) - 1:
                    print(" ", end="")
        print()
