""" Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible
  to continuously remove digits from left to right, and remain prime at each 
  stage: 3797, 797, 97, 7. Similarly we can work from right to left: 3797, 379, 
  37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to
  right and right to left.
NOTE: 2,3,5, and 7 are not considered to be truncatable primes.
https://projecteuler.net/problem=37
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_generator

# --- Conditions of the problem ---
LIMIT = 11              # Inclusive


# --- Calculation ---
def main():
    primes = set([''])
    truncatable = set()

    # Find truncatable primes until limit reached
    for p in prime_generator():
        if len(truncatable) == LIMIT: break

        p_s = str(p)
        primes.add(p_s)
        # Skip single digit primes
        if len(p_s) == 1: continue

        # Check if prime is left and right truncatable
        for i in range(len(p_s)):
            if p_s[i:] not in primes or p_s[:i] not in primes: break
        # Store it if so
        else: truncatable.add(p)


    # --- Output ---
    print(sum(truncatable)) # 748,317
    return
