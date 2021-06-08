#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    inherits from Base, class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def area(self):
        return self.__height * self.__width

    def display(self):
        for lines in range(self.__y):
            print("")
        for i in range(self.__height):
            for espace in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.__width = args[1]
            elif len(args) == 3:
                self.__height = args[2]
            elif len(args) == 4:
                self.__x = args[3]
            elif len(args) == 5:
                self.__y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    def __str__(self):
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
