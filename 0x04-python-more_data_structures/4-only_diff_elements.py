#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_one_only = set_1.difference(set_2)
    set_two_only = set_2.difference(set_1)
    combined_set = set_one_only | set_two_only
    return combined_set
