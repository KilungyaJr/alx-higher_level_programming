#!/usr/bin/python3
def magic_calculation(a, b):
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return result
