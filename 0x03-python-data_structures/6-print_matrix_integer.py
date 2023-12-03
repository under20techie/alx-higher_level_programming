#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if not len(matrix[i]):
            print()
            break
        print("{}".format(matrix[i]))
