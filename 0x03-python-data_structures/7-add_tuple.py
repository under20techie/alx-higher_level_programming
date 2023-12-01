#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        t_left = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        t_left = (0, 0)
    else:
        t_left = tuple_a

    if len(tuple_b) == 1:
        t_right = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        t_right = (0, 0)
    else:
        t_right = tuple_b
    return t_left[0] + t_right[0], t_left[1] + t_right[1]
