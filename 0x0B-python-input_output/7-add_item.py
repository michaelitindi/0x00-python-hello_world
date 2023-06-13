#!/usr/bin/python3
""" script that adds all arguments to a Python list"""


import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

new_items = sys.argv[1:]
updated = data + new_items
save_to_json_file(updated, filename)
