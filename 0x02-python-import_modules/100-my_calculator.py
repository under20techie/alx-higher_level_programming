#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not argv[2] or argv[2] not in "+-/*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]
    if sign == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sign == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sign == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sign == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
