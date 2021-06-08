#!/usr/bin/python3
"""
class square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        """
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
        return str("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        if args and args != None:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.size = args[1]
            elif len(args) == 3:
                self.x = args[2]
            elif len(args) == 4:
                self.y = args[3]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
