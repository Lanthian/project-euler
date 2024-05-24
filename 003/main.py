""" Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
https://projecteuler.net/problem=3
"""

__author__ = "Liam Anthian"

# --- Imports ---
from primes import prime_factors

# --- Conditions of the problem ---
PRODUCT = 600851475143


# --- Output ---
print(prime_factors(PRODUCT)[-1]) # 6,857
