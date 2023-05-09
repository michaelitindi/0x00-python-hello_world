#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            result = chr(ord(i) - 32)
        print("{:s}".format(i), end='')
