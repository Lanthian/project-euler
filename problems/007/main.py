""" 10001st Prime

By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the
  6th prime is 13.
What is the 10001st prime number?
https://projecteuler.net/problem=7
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_generator

# --- Conditions of the problem ---
NUMBER = 10001


# --- Output ---
def main():
    i = 1
    for p in prime_generator():
        if i == NUMBER:
            print(p) # 104,743
            break
        i += 1


    # --- Further explored ---
    """
    # Single line solution supplied @ https://stackoverflow.com/a/54333239
    #   by user lovasoa https://stackoverflow.com/users/3579309/
    print(next(x for i,x in enumerate(prime_generator()) if i+1==NUMBER))
    """
  