#!/usr/bin/python3
"""
print square
using the # character

"""


def print_square(size):
    """
    print square
    using the # character

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size <= 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
