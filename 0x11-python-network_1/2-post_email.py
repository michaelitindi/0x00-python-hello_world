#!/usr/bin/python3
""" sends a POST request to the passed URL """
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email_value = sys.argv[2]
data = urllib.parse.urlencode({"email": email_value}).encode("utf-8")
with urllib.request.urlopen(url, data=data) as response:
    print(response.read().decode("utf-8"))
