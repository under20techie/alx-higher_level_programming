#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    max_num = 0
    for c in my_list:
        if c > max_num:
            max_num = c
    return max_num
