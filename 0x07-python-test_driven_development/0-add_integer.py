#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return int(a) + int(b)
    except Exception as e:
        if isinstance(a, int) is False:
            raise TypeError("a must be an integer")
        if isinstance(b, int) is False:
            raise TypeError("b must be an integer")
