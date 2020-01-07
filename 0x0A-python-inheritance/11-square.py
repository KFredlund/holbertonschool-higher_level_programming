#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherting from Rectangle class
    """

    def __init__(self, size):
        """Function that makes a square"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
