#!/usr/bin/python3
"""Contains isWinner function to determine
who the winner of each game"""


def isWinner(x, nums):
    def sieve(n):
        """Genetare list of prime numbers"""
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return primes

    def canWin(n):
        """check winner of each round"""
        primes = sieve(n)
        remaining = set(range(1, n + 1))
        for p in primes:
            if p in remaining:
                remaining.difference_update(range(p, n + 1, p))
            else:
                for multiple in range(p, n + 1, p):
                    if multiple in remaining:
                        remaining.remove(multiple)
        return len(remaining) > 0

    maria_wins = sum(canWin(n) for n in nums)

    if maria_wins > x - maria_wins:
        return "Maria"
    elif maria_wins < x - maria_wins:
        return "Ben"
    else:
        return None
