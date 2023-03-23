#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Get the no if minimum combination
    """
    if total <= 0:
        return 0
    amt = [float('inf')] * (total + 1)
    amt[0] = 0

    for coin in coins:
        for fewest in range(coin, total + 1):
            if amt[fewest - coin] != float('inf'):
                amt[fewest] = min(amt[fewest], amt[fewest - coin] + 1)
                # amt[fewest] += 1
    if amt[total] != float('inf'):
        return amt[total]
    return - 1
