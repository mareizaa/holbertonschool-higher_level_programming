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
