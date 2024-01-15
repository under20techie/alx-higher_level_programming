#!/usr/bin/python3
""" Contains safe_print_integer """


def safe_print_integer(value):
    """ prints an integer  """

    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
