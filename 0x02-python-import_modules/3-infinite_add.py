#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    argc = len(argv) - 1

    args = sys.argv
    result = 0
    for i in range(1, argc + 1):
        result += int(args[i])
    print("{:d}".format(result))
