#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for c in my_list:
        if c > int(max_num):
            max_num = c
    return max_num
