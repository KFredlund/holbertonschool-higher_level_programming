#!/usr/bin/python3
def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False."""
    if issubclass(int, a_class) is True:
        return True
    return False
