#!/usr/bin/python3
"""Square that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class representing square """

    def __init__(self, size):
        """initialize square """
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """area of square"""
        return self.__size ** 2
