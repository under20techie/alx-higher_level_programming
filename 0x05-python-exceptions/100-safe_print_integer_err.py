#!/usr/bin/python3
"""Contains safe_print_integer_err """
import sys


def safe_print_integer_err(value):
    '''Prints an integer '''

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
