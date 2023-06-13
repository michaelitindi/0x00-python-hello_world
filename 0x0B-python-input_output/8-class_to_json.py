#!/usr/bin/python3
""" returns the dict with simple data structure  """


def class_to_json(obj):
    """returns dictionary description """
    return obj.__dict__
