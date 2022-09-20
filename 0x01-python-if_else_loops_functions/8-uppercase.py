#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            upper_ch = chr(ord(ch) - 32)
        else:
            upper_ch = ch
        print("{:s}".format(upper_ch), end="")
    print("")
