#!/usr/bin/python3
""" returns the number of characters written:"""


def write_file(filename="", text=""):
    """ returns no of chars"""
    with open(filename, 'w', encoding='utf-8') as file:
        res = file.write(text)
    return res
