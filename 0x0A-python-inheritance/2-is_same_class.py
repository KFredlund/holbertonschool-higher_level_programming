#!/usr/bin/python3
def is_same_class(obj, a_class):
    """A function that returns True if the object is exactly
    an instance of the specified class"""
    if issubclass(a_class, type(obj)) is True:
        if a_class is not object:
            return True
    else:
        return False
