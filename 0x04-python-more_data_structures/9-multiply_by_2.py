#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = a_dictionary.copy()
    for value in mul_dict.keys():
        mul_dict[value] *= 2
    return mul_dict
