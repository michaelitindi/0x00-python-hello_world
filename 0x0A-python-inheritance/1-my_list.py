#!/usr/bin/python3
""" Class that inherits from another class """


class MyList(List):
    """ Class mylist"""

    def print_sorted(self):
        """Prints in sorted order"""
        print(sorted(List))
