#!/usr/bin/python3
"""
Min Oerations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to
        reach n 'H' characters. If n is impossible to
        achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    d = 2  # Start by copying 1 'H' and pasting it

    while n > 1:
        while n % d == 0:
            n /= d
            operations += d
        d += 1

    return operations
