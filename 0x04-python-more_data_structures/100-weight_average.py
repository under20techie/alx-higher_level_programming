#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or any(len(pair) != 2 for pair in my_list):
        return 0
    num = div = 0
    for i , j in my_list:
        num += i * j
        div += j
    return num / div 
