#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0 and idx > len(my_list):
            return None
        else:
            return my_list[idx]
