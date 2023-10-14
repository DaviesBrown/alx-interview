#!/usr/bin/python3
"""
minimum oeration
"""


def minOperations(n: int) -> int:
    """
    finds the minimum no of operations to get a string
    """
    if type(n) is not int:
        return 0
    if n <= 1:
        return 0
    
    char_len = 1
    ops = 0
    copy_value = 0

    while char_len < n:
        if n % char_len == 0:
            copy = char_len
            char_len += copy
            ops += 2
        else:
            char_len += copy
            ops += 1

    return ops
