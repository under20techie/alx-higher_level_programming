#!/usr/bin/python3
"""Contains safe_print_division """


def safe_print_division(a, b):
    '''Divides two integers and prints result '''

    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
