#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        l = len(matrix)
        for i in range(l):
            for width in range(len(matrix[i])):
                    if width != len(matrix) - 1:
                        print("{:d} ".format(matrix[i][width]), end="")
                    else:
                        print("{:d}".format(matrix[i][width]), end="")
            print()
