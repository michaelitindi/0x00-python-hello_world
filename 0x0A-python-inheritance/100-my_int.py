#!/usr/bin/python3
""" class has operators inverted"""


class MyInt(int):
    """inverted operators """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
