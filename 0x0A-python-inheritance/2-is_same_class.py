#!/usr/bin/python3
"""returns True if the object is exactly an instance of class """


def is_same_class(obj, a_class):
    """ Returns true if exactly instance"""
    return type(obj) is a_class
