#!/usr/bin/python3
"""Matrix multiplication """


def matrix_mul(m_a, m_b):
    """matrix_multiplication"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_b:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if not row:
            raise ValueError("m_a can't be empty")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if not row:
            raise ValueError("m_b can't be empty")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
