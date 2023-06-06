#!/usr/bin/python3
"""Creating a class with no object or attribute """


class LockedClass:
    """Cannot create instance unless attribute is first name """
    __slots__ = ["first_name"]
