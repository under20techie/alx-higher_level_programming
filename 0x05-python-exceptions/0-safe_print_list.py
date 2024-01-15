#!/usr/bin/python3
"""Prints the x elements of a list """


def safe_print_list(my_list=[], x=0):
    """Prints x element of a list """
    i = 0
    for m in range(x):
        try:
            print("{}".format(my_list[m]), end="")
            i += 1
        except Exception:
            break
    print()
    return i
