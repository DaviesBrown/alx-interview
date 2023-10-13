#!/usr/bin/python3
"""
minimum oeration
"""


def minOperations(n):
    """
    finds the minimum no of operations to get a string
    """
    if type(n) is not int:
        return 0
    if n <= 1:
        return 0

    op = 0
    chars = 1
    copy = 1

    while chars < n:
        if n % chars == 0:
            copy = chars
            op += 1
        if chars != n:
            chars += copy
            op += 1
        else:
            break

    return op
