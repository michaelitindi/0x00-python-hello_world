#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        first = sentence[0]
    else:
        first = None
    length = len(sentence)
    return length, first
