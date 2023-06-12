#!/usr/bin/python3
"""class basegeometry"""


class BaseGeometry:
    """class with two methods"""

    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """validates value """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
