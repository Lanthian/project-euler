""" Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the
  digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
  also prime.
What is the largest n-digit pandigital prime that exists?
https://projecteuler.net/problem=41
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import pandigital
from common.primes import prime_sieve

# --- Conditions of the problem ---
MAX_DIGITS = 9


# --- Calculation & Output ---
def main():
    # Generate list of primes - bit of a slow implementation...
    primes = prime_sieve(7654321)

    # Working backwards, first pandigital number is what we're looking for
    for i in reversed(primes):
        i_s = str(i)
        if pandigital(i_s, len(i_s)): 
            print(i) # 7,652,413
            break
    

# --- Further Research ---
"""User 'gamma' notes on the projecteuler thread that 9 & 8 aren't possible,
since 1+2+...+9=45 and 1+2+...+8=36, both always divisible by 3. We can 
start with a lower ceiling in turn, instead using 7654321 and searching 
backwards from there."""
