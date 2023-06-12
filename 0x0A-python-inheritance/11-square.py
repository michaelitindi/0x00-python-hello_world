#!/usr/bin/python3
"""Square that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class representing square """

    def __init__(self, size):
        """initialize square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self):
        """prints the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
