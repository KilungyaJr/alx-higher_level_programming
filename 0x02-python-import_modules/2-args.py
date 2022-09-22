#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    elif argc > 1:
        print("{} arguments:".format(argc))

    args = sys.argv
    for i in range(1, argc + 1):
        print("{}: {}".format(i, args[i]))
