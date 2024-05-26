""" Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million.
https://projecteuler.net/problem=10
"""

__author__ = "Liam Anthian"

# --- Imports ---
from primes import prime_generator

# --- Conditions of the problem ---
LIMIT = 2 * 10**6


# --- Calculation ---
sum = 0
for p in prime_generator():
    if p >= LIMIT: break
    sum += p
    print(p)


# --- Output ---
print(sum)


# CURRENTLY WAY TOO SLOW



