#!/usr/bin/python3
def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object"""
    objList = [method_name for method_name in dir(obj)
               if callable(getattr(obj, method_name))]
    return objList
