#!/usr/bin/python3
"""This is a module"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                st = st + str(self.print_symbol)
            if i < self.__height - 1:
                st = st + '\n'
        return st

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            a = Rectangle.area(rect_1)
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle):
            b = Rectangle.area(rect_2)
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if a > b:
                return rect_1
        elif b > a:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        a = size
        b = size
        return cls(a, b)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
