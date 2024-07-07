""" Distinct Primes Factors

The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 x 7
    15 = 3 x 5.
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2^2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19
Find the first four consecutive integers to have four distinct prime factors 
  each. What is the first of these numbers?
https://projecteuler.net/problem=47
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen
from common.primes import powered_prime_factors

# --- Conditions of the problem ---
CONSECUTIVE = 3
FACTORS = 3


# --- Calculation & Output ---
def main():
    # Prestore necessary prime factors for previous numbers
    stored = {k: powered_prime_factors(k) for k in range(1, CONSECUTIVE)}

    for i in int_gen(CONSECUTIVE):
        stored[i] = powered_prime_factors(i)

        # Check if prime factors are distinct
        facs = set()
        for j in range(i+1 - CONSECUTIVE, i+1):
            if len(stored[j]) != FACTORS: break
            facs.update(stored[j])
        
        if len(facs) == CONSECUTIVE * FACTORS: 
            print(i+1 - CONSECUTIVE)
            break
            
    return
