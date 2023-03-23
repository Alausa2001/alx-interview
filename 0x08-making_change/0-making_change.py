#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins: list, total: int) -> int:
    """
    Get the no if minimum combination
    """
    if total <= 0:
        return 0
    fewest = 0
    target = 0
    current = 0
    rev_coins = sorted(coins, reverse=True)
    coin_index = 0
    length = len(rev_coins)

    while (target < total) and (coin_index < length):
        target = current + rev_coins[coin_index]
        if target < total:
            fewest += 1
            current = target
        elif target > total:
            target -= rev_coins[coin_index]
            coin_index += 1
        elif target == total:
            return fewest + 1
    return -1
