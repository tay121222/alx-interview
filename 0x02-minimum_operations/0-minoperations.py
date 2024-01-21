#!/usr/bin/python3
"""Contains method minOperations"""
import math


def minOperations(n):
    """method that calculates the fewest number of
    operations needed to result in exactly"""
    if n == 1:
        return 0
    result = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            result += i
        i += 1
    if n > 1:
        result += n

    return result
