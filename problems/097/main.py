""" Large Non-Mersenne Prime

The first known prime found to exceed one million digits was discovered in 1999, 
  and is a Mersenne prime of the form 2^6972593 - 1; it contains exactly 2098960
  digits. Subsequently other Mersenne primes, of the form 2^p - 1, have been 
  found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 
  2357207 digits: 28433 * 2^7830457 + 1.
Find the last ten digits of this prime number.

https://projecteuler.net/problem=97
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time

# --- Conditions of the problem ---
POWERS = 7830457
MULT = 28433
DIGITS = 10


# --- Calculation ---
def main():
    start = time.time()

    n = 1
    for i in range(POWERS):
        n *= 2
        if n >= 10**DIGITS:
            n = int(str(n)[-10:])
    
    n *= MULT
    n += 1


    # --- Output ---
    print("Time:", time.time() - start)
    print(str(n)[-10:]) # 8739992577
    return
