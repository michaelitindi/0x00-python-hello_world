#!/usr/bin/python3
""" Rectangle class that inherits from basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle inheriting base geometry"""

    def __init__(self, width, height):
        """ initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
