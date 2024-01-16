#!/usr/bin/python3
'''Prints square '''


def print_square(size):
    """Prints square func """

    if type(size) is not int \
            or type(size) is float and size < 0.0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
