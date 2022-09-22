#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    from sys import argv
    argc = len(argv) - 1

    args = sys.argv
    for i in range(1, argc + 1):
        a = int(args[1])
        b = int(args[3])
        operator = args[2]
    result = 0
    math_ops = ["+", "-", "*", "/"]
    if int(argc) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif operator not in math_ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif int(argc) == 3:
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
