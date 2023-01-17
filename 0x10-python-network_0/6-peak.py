#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers using
a divide and conquer approach which has a complexity of O(log(n))
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak in a list of unsorted integers
    using a divide and conquer approach.
    :param list_of_integers: A list of unsorted integers
    :return: A peak element from the list
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n < 3:
        return max(list_of_integers)
    mid = n // 2
    if list_of_integers[mid - 1] < list_of_integers[mid] \
       and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid - 1] < list_of_integers[mid]:
        return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[:mid])
