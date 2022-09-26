#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    if length == 0:
        return (0, "None")
    else:
        return (length, first)
