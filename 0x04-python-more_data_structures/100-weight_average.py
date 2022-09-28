#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    res = 0
    res2 = 0
    for x, y in my_list:
        res = res + x * y
        res2 = res2 + y
    return res / res2
