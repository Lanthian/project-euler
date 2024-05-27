"""primes.py: Functions for handling prime numbers - generation and checking."""

__author__ = "Liam Anthian"

# --- Imports ---
from math import sqrt


# First seen in 005 - Smallest Multiple
def factor(product: int, i: int) -> bool:
    """Returns True if `i` is a factor of `product`. False if otherwise."""
    return product % i == 0

# First seen in 003 - Largest Prime Factor
def prime(num: int, primes: list[int]) -> bool:
    """Checks if an int `num` is prime, according to possible factors in 
    `primes`. Returns a boolean."""
    # Break early if past last possible factor of num
    limit = sqrt(num)
    for p in primes:
        if p > limit: return True
        elif factor(num, p): return False
    return True

# First seen in 003 - Largest Prime Factor
def prime_generator():
    """A generator for prime numbers - uses `prime()` in prime construction."""
    yield 2
    yield 3
    primes = [2,3]

    i = 1
    while(True):
        # Generate primes via 6n-1, 6n+1
        for shift in [-1,1]:
            a = 6 * i + shift

            # Check if number is prime - yield if so
            if prime(a, primes):
                primes.append(a)
                yield a
        
        # Increment
        i += 1

# First seen in 003 - Largest Prime Factor
def prime_factors(product: int) -> list[int]:
    """Takes a number `product` and finds and returns a list of all prime 
    factors that build it."""
    factors = []

    # Incrementally generate primes and check if they are factors of product
    for p in prime_generator():
        while factor(product, p):
            # Store and remove factor from product
            factors.append(p)
            product = product//p

        # Check for cut off
        if p > product or product == 0: break
    return factors

# First seen in 010 - Summation of Primes
def prime_sieve(limit: int) -> list[int]:
    """Eratosthenes Sieve: Generates all primes up to `limit` (not inclusive) by 
    filtering out factors as it works up the range of possible primes."""
    primes = [1]*(limit+1)
    primes[0] = 0
    primes[1] = 0

    for i in range(2, limit):
        # If a prime, remove all greater composites
        if primes[i]: 
            for j in range(i**2, limit, i):
                primes[j] = 0

    return [p*i for i,p in enumerate(primes) if p]
