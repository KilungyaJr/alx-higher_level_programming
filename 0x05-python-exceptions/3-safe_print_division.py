#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
        #print("{} / {} = {}".format(a, b, result))
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
