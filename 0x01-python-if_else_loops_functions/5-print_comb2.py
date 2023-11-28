#!/usr/bin/python3
num1 = 0
num2 = 0
while (num1 < 10):
    num2 = 0
    while(num2 < 10):
        print("{}{}".format(num1, num2), end="")
        if num1 != 9 or num2 != 9:
            print(", ", end="")
        else:
            print()
        num2 += 1
    num1 += 1
