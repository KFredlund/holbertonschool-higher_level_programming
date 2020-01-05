#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for col_space in range(self.__position[0]):
                    print(" ", end="")
                for s in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
