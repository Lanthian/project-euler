""" Coin Paritions

Let p(n) represent the number of different ways in which n coins can be 
  separated into piles. For example, five coins can be separated into piles in 
  exactly seven different ways, so p(5) = 7.
Find the least value of n for which p(n) is divisible by one million.

https://projecteuler.net/problem=78
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen
from common.primes import factor

# --- Conditions of the problem ---
DIVISOR = 10**6

sums = {}

# Modified from 031 - Coin Sums
def simpler_sum_to(curr: int, goal: int, option_start: int=1) -> int:
    """Takes a current integer value `curr`, a `goal` integer value, and a 
    starting integer `option_start` from which integer sums are built to reach
    `goal`. Via recursion, returns an integer of the number of possible path 
    permutations to goal."""
    if curr == goal: return 1

    # Reuse previous sums
    if goal not in sums: sums[goal] = {}
    if curr not in sums[goal]: sums[goal][curr] = {}
    if option_start in sums[goal][curr]: return sums[goal][curr][option_start]

    else:
        # For each possible action from current, check sum sub paths to goal
        result = 0
        for n in int_gen(option_start):
            next_val = curr + n

            if next_val > goal: break
            
            else:
                # Add total (recursive) valid sub paths to result
                result += simpler_sum_to(next_val, goal, n)
        
        sums[goal][curr][option_start] = result
        return result


# --- Calculation ---
def main():
    for i in int_gen(1):
        result = simpler_sum_to(0, i)
        print(i, ":", result)
        if factor(result, DIVISOR): break


    # --- Output ---
    print(result) 
    return
