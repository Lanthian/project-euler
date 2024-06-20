""" Quadratic Primes

Euler discovered the remarkable quadratic formula:
    n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer 
  values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 is 
  divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
  divisible by 41.
The incrtedible formula n^2 - 79n + 1601 was discovered, which produces 80 
  primes for the consecutive values 0 <= n <= 79. The product of coefficients, 
  -79 and 1601, is -126479.
Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| <= 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression 
  that produces the maximum number of primes for consecutive values of n, 
  starting with n = 0.
https://projecteuler.net/problem=27
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_sieve

# --- Conditions of the problem ---
A_RANGE = range(-999,1000)
B_RANGE = prime_sieve(1001) # b has to be a prime given n = 0 must be a prime

A_LIMIT = -999          # Inclusive
B_LIMIT = 1000          # Inclusive


def int_gen(start: int):
    """A generator for increasing integer numbers - starts at `start` (incls)"""
    while(True):
        yield start
        start += 1


# --- Calculation ---
def main():
    # primes = set(prime_sieve(100000))
    #
    # best = (None, None)
    # best_streak = 0
    #
    # for b in B_RANGE:
    #     for a in range(-abs(b),1000):
    #         quad = lambda x: x**2 + a*x + b
    #         streak = 0
    #
    #         for x in int_gen(0):
    #             if quad(x) in primes: streak += 1
    #             else: break
    #        
    #         if streak > best_streak: 
    #             # print((a,b), streak, ":", b / a)  # temp
    #             best_streak = streak
    #             best = (a,b)


    # --- Further explored ---
    """Through experimentation, noticed a pattern. Exploit it here for faster
    calculation. Limits set must permit pre calculated a & b."""
    prod = None
    a = -1
    b = 41
    i = 1
    # length = 41

    # Loop through pattern until max prime generation streak found for limits
    while (a >= A_LIMIT and b <= B_LIMIT): 
        prod = a * b
        a -= 2
        b += 2*i
        i += 1
        # length += 1


    # --- Output ---
    # print(best[0] * best[1]) # -59,231
    print(prod) # -59,231
    return
