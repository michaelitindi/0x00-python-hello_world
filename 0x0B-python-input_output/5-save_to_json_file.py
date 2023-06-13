#!/usr/bin/python3
""" function that saves object to file  """


import json


def save_to_json_file(my_obj, filename):
    """ saves object to file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
