#!/usr/bin/python3
""" adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """ adds attribute"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
