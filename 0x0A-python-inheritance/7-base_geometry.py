#!/usr/bin/python3
"""This is my class"""


class BaseGeometry():
    """This is my class"""
    def area(self):
        """Instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError("{:} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:} must be greater than 0".format(name))
