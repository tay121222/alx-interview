#!/usr/bin/python3
"""Contains isWinner function to determine
who the winner of each game"""


def isWinner(x, nums):
    """determine who the winner of each game"""
    def can_win(round_nums):
        """Check if Maria can win the current round"""
        remaining = list(range(2, max(round_nums) + 1))
        for num in range(2, max(round_nums) + 1):
            if is_prime(num):
                remaining = [n for n in remaining if n % num != 0]
        return len(remaining) % 2 == 1

    def is_prime(num):
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(range(1, n + 1)):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
