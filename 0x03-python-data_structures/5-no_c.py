#!/usr/bin/python3
def no_c(my_string):
    alt_string = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            alt_string += i

    return alt_string
