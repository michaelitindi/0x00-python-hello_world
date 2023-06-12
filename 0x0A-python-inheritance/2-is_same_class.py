#!/usr/bin/python3
""" function that returns True if the object is exactly an instance of the specified class  """


def is_same_class(obj, a_class):
    """ Returns true if exactly instance"""
    return type(obj) is a_class
