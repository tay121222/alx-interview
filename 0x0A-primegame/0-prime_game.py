#!/usr/bin/python3
"""Contains isWinner function to determine
who the winner of each game"""


def isWinner(x, nums):
    """Determine the winner of the game"""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        rounds_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        if not primes_set:
            ben_wins += 1
            continue

        is_maria_turn = True

        while primes_set:
            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]
            is_maria_turn = not is_maria_turn

        if is_maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


def is_prime(n):
    """Checks if number is prime number"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Generate Prime number"""
    return [n for n in range(start, end + 1) if is_prime(n)]
