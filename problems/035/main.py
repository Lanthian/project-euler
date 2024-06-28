""" Circular Primes

The number, 197, is called a circular prime because all rotations of the digits:
  197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2,3,5,7,11,13,17,31,37,71,73,79,97.
How many circular primes are there below one million?
https://projecteuler.net/problem=35
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_sieve

# --- Conditions of the problem ---
LIMIT = 10**6           # Exclusive


def int_circulations(x: int) -> set[int]:
    """Returns an unordered set of circulations of a number `x`. For example, x
    = 123 would return some sorting of {123, 231, 312}."""
    x_s = str(x)
    # Use a set to drop palindrome circulations
    return {int(x_s[i:]+x_s[:i]) for i in range(len(x_s))}


# --- Calculation ---
def main():
    primes = set(prime_sieve(LIMIT))

    seen = set()
    circular = 0

    for p in primes:
        # Skip already observed primes
        if p in seen: continue

        else: 
            # Generate and store circulations
            circulations = int_circulations(p)
            seen.update(circulations)

            # Continue loop if any of the circulations aren't prime
            for num in circulations:
                if num not in primes: break
            # Otherwise, +1 for each circulation
            else: circular += len(circulations)


    # --- Output ---
    print(circular) # 55
    return
