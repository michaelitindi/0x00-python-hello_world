#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ascending = sorted(a_dictionary.keys())
    for i in ascending:
        value = a_dictionary[i]
        print("{} : {}".format(i, value))
