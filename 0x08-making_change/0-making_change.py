#!/usr/bin/python3
"""Contains method makeChange"""


def makeChange(coins, total):
    """determine the fewest number of coins needed
    to meet a given amount total"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    remaining_amount = total
    for coin in coins:
        num_coins += remaining_amount // coin
        remaining_amount %= coin

    if remaining_amount == 0:
        return num_coins
    else:
        return -1
