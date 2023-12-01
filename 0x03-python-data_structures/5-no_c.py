#!/usr/bin/python3
def no_c(my_string):
    my_string1 = ""
    for c in my_string:
        if c not in "cC":
            my_string1 += c
    return my_string1
