#!/usr/bin/python3
"""Contains text_indentation func """


def text_indentation(text):
    """Prints text_indentation """

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for c in text.strip():
        if c in ".?:" and flag == 0:
            print("{}\n".format(c))
            flag = 1
        elif flag == 1 and c == ' ':
            continue
        else:
            print(c, end='')
            flag = 0
