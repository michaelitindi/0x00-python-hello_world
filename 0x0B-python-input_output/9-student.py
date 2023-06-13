#!/usr/bin/python3
""" Class student with dict representation"""


class Student:
    """attributes and methods """

    def __init__(self, first_name, last_name, age):
        """ intialized student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict representation"""
        return self.__dict__
