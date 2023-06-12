#!/usr/bin/python3
"""returns True if the object instance of class that inherited """


def inherits_from(obj, a_class):
    """ Returns true if obj is
    instance of class that inherited from the specified class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
