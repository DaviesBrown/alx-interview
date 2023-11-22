#!/usr/bin/python3
"""
make change module
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determines the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0: return 0
    count = 0
    sorted_coins = sorted(coins, reverse=True)
    for i in sorted_coins:
        while total - i >= 0:
            count += 1
            total = total - i
        if total == 0:
            return count    
    return -1