#!/usr/bin/python3
"""Contains safe_print_integer_err """


def safe_print_integer_err(value):
    '''Prints an intege '''

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e))
