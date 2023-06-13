#!/usr/bin/python3
""" appends text at the end of a file"""


def append_write(filename="", text=""):
    """ appends at the end"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
