#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor init"""
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.__size))

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Update method"""
        if len(args) is not 0 and args is not None:
            for position, arg in enumerate(args):
                if position is 0:
                    self.id = arg
                if position is 1:
                    self.size = arg
                if position is 2:
                    self.x = arg
                if position is 3:
                    self.y = arg
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
