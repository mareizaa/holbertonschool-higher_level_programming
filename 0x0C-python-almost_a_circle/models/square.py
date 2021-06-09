#!/usr/bin/python3
"""
class square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor Square """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """ Sting square """
        return str("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ handle args and kwargs """
        if args:
            a_square = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, a_square[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary"""
        return({"id": self.id, "size": self.size,
                "x": self.x, "y": self.y})
