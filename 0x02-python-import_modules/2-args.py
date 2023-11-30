#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len1 = len(argv)
    if len1 == 2:
        print("{} argument:".format(len1))
    elif len1 > 2:
        print("{} arguments:".format(len1))
    else:
        print("{} arguments.".format(len1))
    for i in range(1, len1):
        print("{}: {}".format(i, argv[i]))
