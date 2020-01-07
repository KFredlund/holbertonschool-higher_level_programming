#!/usr/bin/python3
class MyList(list):
    """
    MyList is a class that inherits from list
    """

    def print_sorted(self):
        """A public instance method that prints a sorted list"""
        print(sorted(self))
