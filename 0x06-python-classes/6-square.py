#!/usr/bin/python3
"""Este es el docstring del módulo"""


class Square:
    """Este es el docstring de la clase"""
    def __init__(self, size=0, position=(0, 0)):
        """Este es el docstring de la instancia"""
        if isinstance(size, int):
            self.__size = size
            self.__position = position
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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for pos in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                for pos in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """to set it"""
        self.__position = value
        if value < 0:
            raise TypeError("position must be a tuple of \
                2 positive integers")
