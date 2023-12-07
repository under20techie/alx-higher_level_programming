#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda col: [x * 2 for x in col], matrix))
