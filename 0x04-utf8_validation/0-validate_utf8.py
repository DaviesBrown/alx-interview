#!/usr/bin/python3
"""
validate utf8
"""
from typing import List
from encodings.utf_8 import decode
print(5)
print(bytes([256]))

def validUTF8(data: List[int]) -> bool:
    """
    determines if a given dataset is valid UTF-8 encoding
    """
    try:
        decode(bytes(data))
    except ValueError:
        return False
    return True
