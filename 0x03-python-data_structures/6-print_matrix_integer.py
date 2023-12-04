#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not len(row):
            print()
            break
        for i in range(len(row)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(row[i]), end="")
        print()
