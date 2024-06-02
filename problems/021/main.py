""" Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
  which divide evenly into n).
If d(a) = b and d(b) = a, where a!=b, then a and b are an amicable pair and each 
  of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110; 
  therefore d(220) = 284. The proper divisors of 220 are 1,2,4,5,10,11,20,22,44,
  55 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
https://projecteuler.net/problem=21
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import factors, prime_sieve

# --- Conditions of the problem ---
LIMIT = 10000       # Not inclusive


def proper_divisor_sum(num: int) -> int:
    """Shorthand function to return the proper divisor sum of a number `num`."""
    return sum(factors(num).difference([num]))


# --- Calculation ---
def main():
    amicable = set()
    not_amicable = set()

    # Filter out len(primes) numbers
    primes = set(prime_sieve(LIMIT))

    for m in range(2, LIMIT):
        # Skip primes - cannot be amicable
        if m in primes: continue
        # Skip calculating numbers already labelled
        if m in amicable or m in not_amicable: continue

        s = proper_divisor_sum(m)
        # Cannot be amicably paired with self
        if s == m: not_amicable.add(m)
        else:
            next = proper_divisor_sum(s)
            if next == m: amicable.update([m,s])
            else: not_amicable.update([m,s,next])


    # --- Output ---
    print(sum(amicable)) # 31,626
    return


# --- Further thoughts ---
"""
No prime number can be amicable - perhaps sieve primes once before running to
avoid trying to find all factors for all primes throughout?
"""
