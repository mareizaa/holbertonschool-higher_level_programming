#!/usr/bin/python3
"""Create a Class"""


class Student():
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list or attrs is None:
            return self.__dict__
        new = {}
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
            if i in self.__dict__:
                new[i] = self.__dict__[i]
        return new
