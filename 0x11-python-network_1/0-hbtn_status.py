#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("- type: {}".format(type(body)))
    print("- content: {}".format(body))
    print("- utf8 content: {}".format(body.decode("utf-8")))
