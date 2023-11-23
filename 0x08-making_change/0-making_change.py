#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
"""
import sys


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given total.

    Parameters:
    - coins (list): A list of coin values.
    - total (int): The target total amount.

    Returns:
    - int: The fewest number of coins needed to meet the total. If the total
      cannot be met by any combination of coins, return -1.
    """
    table = [float('inf')] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] != float('inf') else -1
