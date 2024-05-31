""" Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million.
https://projecteuler.net/problem=10
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_sieve

# --- Conditions of the problem ---
LIMIT = 2 * 10**6


# --- Calculation & Output ---
def main():
    print(sum(prime_sieve(LIMIT))) # 142,913,828,922
