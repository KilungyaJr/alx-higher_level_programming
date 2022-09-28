#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    targets = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            targets.append(key)
    for i in targets:
        del a_dictionary[i]
    return a_dictionary
