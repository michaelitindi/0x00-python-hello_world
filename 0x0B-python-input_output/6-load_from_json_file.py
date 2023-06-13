#!/usr/bin/python3
""" function that loads from json file  """


import json


def load_from_json_file(my_obj, filename):
    """ loads from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
