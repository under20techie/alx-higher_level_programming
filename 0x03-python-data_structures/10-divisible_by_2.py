#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_false = []
    for c in my_list:
        if c % 2 == 0:
            true_false.append(True)
        else:
            true_false.append(False)
    return true_false
