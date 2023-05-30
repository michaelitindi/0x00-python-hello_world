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

    def area(self):
        """
        Returns the current square area

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for the size attribute.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        Prints the square using the character '#'.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
