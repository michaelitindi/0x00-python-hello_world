#!/usr/bin/python3
""" Class representing a square """


class Square:
    """ Class square with size attribute (private) """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size

         Args:
             size: size of square
             position: position of square
         """
         self.size = size
         self.position = position


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

    @property
    def position(self):
        """
        Getter method for the position attribute.


        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


    def my_print(self):
        """
        Prints the square using the character '#'.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
