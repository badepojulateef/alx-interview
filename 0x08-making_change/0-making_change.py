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
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    if coins and coins[-1] > total:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
