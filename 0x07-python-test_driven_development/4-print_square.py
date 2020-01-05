#!/usr/bin/python3
def print_square(size):
    """Function that prints a square with the character #
    Args:
        size: size of the square
    Returns:
        A square of #s the size of @size
    Raises:
        TypeError: If size is not an int, or if a float and < 0
        ValueError: if size is less than 0
    Doctest Examples:
        see dir: /tests/4-print_square.txt
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for element in range(size):
            print("#", end="")
        print()
