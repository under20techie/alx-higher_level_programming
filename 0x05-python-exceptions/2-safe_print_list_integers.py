#!/usr/bin/python3
"""Contains safe_print_list_integers """


def safe_print_list_integers(my_list=[], x=0):
    """Prints integers """

    no_ofnum = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_ofnum += 1
        except (TypeError, ValueError):
            continue
    print()
    return no_ofnum
