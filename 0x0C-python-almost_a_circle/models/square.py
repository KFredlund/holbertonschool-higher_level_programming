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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__size = value
