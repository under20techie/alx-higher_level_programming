#!/usr/bin/python3
num1 = 0
while (num1 < 100):
    if num1 != 99:
        print("{:02d}, ".format(num1), end="")
    else:
        print("{:02d}".format(num1))
    num1 += 1
