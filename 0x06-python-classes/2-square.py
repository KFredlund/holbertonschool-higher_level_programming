#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
    try:
        sizeInt = isinstance(size, int)
    except TypeError:
        print("size must be an integer")
    try:
        sizeInt >= 0 is True
    except ValueError:
        print("size must be >= 0")
