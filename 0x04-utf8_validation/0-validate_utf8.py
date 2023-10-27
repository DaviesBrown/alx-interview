#!/usr/bin/python3
"""
validate utf8
"""
from typing import List
from encodings.utf_8 import decode


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given dataset is valid UTF-8 encoding
    """
    succ10 = 0
    for i in data:
        b = bin(i).replace('0b', '').rjust(8, '0')
        if len(b) > 8:
            b = b[1:]
        if succ10 != 0:
            succ10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
            succ10 = len(b.split('0')[0]) - 1
    return True
