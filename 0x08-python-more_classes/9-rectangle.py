#!/usr/bin/python3
""" Class defining a rectangle"""


class Rectangle:
    """ Class rectangle with height and width attribute """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height

         Args:
            width: width of rectangle
            height: height of rectangle

         """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print a rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"
        return result[:-1]

    def __repr__(self):
        """ String representation of rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
