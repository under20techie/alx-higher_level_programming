#!/usr/bin/python3
"""Executes a function safely """
import sys


def safe_function(fct, *args):
    """ Execeutes a func safely """

    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
