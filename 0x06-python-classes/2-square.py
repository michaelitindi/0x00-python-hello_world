#!/usr/bin/python3
""" Class representing a square """


class Square:
    """ Class square with size attribute (private) """

    def __init__(self, size=0):
        """Initialize square with size

         Args:
             size: size of square

         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
