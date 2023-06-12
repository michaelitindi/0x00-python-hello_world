#!/usr/bin/python3
""" dds a new attribute to an object"""


def add_attribute(obj, name, value):
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
