#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor init"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """String method"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.__size))
