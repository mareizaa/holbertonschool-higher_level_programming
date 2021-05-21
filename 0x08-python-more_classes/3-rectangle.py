#!/usr/bin/python3
"""This is a module"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the instance"""
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter area"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        st = ""
        if self.__height == 0 or self.__width == 0:
            return st

        for i in range(self.__height):
            for j in range(self.__width):
                st = st + '#'
            if i < self.__height - 1:
                st = st + '\n'
        return st
