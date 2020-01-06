#!/usr/bin/python3
class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """Function that raises an expeption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=0):
        """Function that validates value"""
        if isinstance(value, int) is False:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
