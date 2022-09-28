#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    for i in range(len(roman_string)):
        if i+1 != len(roman_string) and\
           nums[roman_string[i]] < nums[roman_string[i+1]]:
            ans = ans - nums[roman_string[i]]

        else:
            ans = ans + nums[roman_string[i]]
    return ans
