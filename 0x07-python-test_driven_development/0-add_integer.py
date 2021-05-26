#!/usr/bin/python3
"""
function that adds two integers
Test that the arguments are integers
Returns the result
"""


def add_integer(a, b=98):
    """
    return a + b
    """
    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    else:
        return a + b

if __name__ == '__main__':
    import doctest
    doctest.testfile("/tests/0-add_integer.txt")
