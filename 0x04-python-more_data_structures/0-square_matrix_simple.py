#!/usr/bin/python3
"Contains square_matrix func"


def square_matrix_simple(matrix=[]):
    """Squares element of a 2 dimensional array"""

    new_matrix = matrix.copy()
    for row in range(len(new_matrix)):
        new_matrix[row] = list(map(lambda x: x ** 2, new_matrix[row]))
    return new_matrix
