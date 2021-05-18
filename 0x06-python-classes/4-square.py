#!/usr/bin/python3
"""Este es el docstring del módulo"""


class Square:
    """Este es el docstring de la clase"""
    def __init__(self, size=0):
        """Este es el docstring de la instancia"""
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it"""
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
