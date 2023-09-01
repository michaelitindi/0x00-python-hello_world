#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(dict(response.headers).get('X-Request-Id'))
