#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        largest_int = my_list[0]
        for i in my_list:
            if i > largest_int:
                largest_int = i
        return largest_int
