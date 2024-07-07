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
from common.primes import powered_prime_factors, prime_sieve

# --- Conditions of the problem ---
CONSECUTIVE = 4
FACTORS = 4


# --- Calculation ---
def main():
    # Trackers
    count = 0
    start = None
    factors = set()

    # Prepare primes
    primes = prime_sieve(1000000)

    # Iterate through numbers until sequence found
    for i in int_gen(644):
        if count == 0: start = i

        p = powered_prime_factors(i, primes)
        count += 1
        factors.update(p)

        # Skip ahead and reset trackers if invalid
        if len(factors) != FACTORS * count: 
            i += CONSECUTIVE -1
            count = 0
            start = None
            factors = set()
            continue

        elif count == CONSECUTIVE: break
    

    # --- Output ---
    print(start) # 134043
    return
