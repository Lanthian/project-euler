""" Prime Summations

It is possible to write ten as the sum of primes in exactly five different ways:
    7+3
    5+5
    5+3+2
    3+3+2+2
    2+2+2+2+2
What is the first value which can be written as the sum of primes in over five 
thousand different ways?

https://projecteuler.net/problem=77
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.primes import prime_generator

# --- Conditions of the problem ---
THRESHOLD = 5000


# First seen in 031 - Coin Sums
def sum_from(goal: int, options: list[int], stored: dict[(int,int): int]={}
             ) -> int:
    """Via recursion, returns an integer of the number of possible path 
    permutations to a `goal` integer value, built from combinations of possible 
    addends listed in `options`. Recursions are stored in `stored` to avoid
    repeat calculation."""
    # Terminating conditions
    if len(options) == 0: return 0
    if goal == 0: return 1

    # Retrieve sum from `stored`, calculating if needed
    best = options[-1]
    tup = (goal,best)
    if tup not in stored: 
        # Recursive steps & `stored` update
        output = 0 if best > goal else sum_from(goal - best, options, stored)
        stored[tup] = output + sum_from(goal, options[:-1], stored)
    return stored[tup]


# --- Calculation & Output ---
def main():
    start = time.time()

    prev = 0
    primes = []
    for p in prime_generator():
        # Iterate over values between current end and next prime
        for goal in range(prev, p):
            # If possible sums exceeds threshold, end reached
            if sum_from(goal,primes) > THRESHOLD:
                print("Time:", time.time() - start)
                print(goal) # 71
                return     
            
        # Add next prime to list of available primes
        primes.append(p)
        prev = p

    # Failure somewhere
    return -1
