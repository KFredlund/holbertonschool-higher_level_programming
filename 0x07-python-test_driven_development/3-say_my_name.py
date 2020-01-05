#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Function that prints 'My name is <first name> <last name>'
    Args:
        first_name: first string
        last_name: second string
    Returns:
        first and last name
    Raises:
        TypeError: if args are not strings
    Doctest Examples:
        see dir: /tests/3-say_my_name.txt
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
