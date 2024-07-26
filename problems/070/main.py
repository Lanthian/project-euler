"""Totient Permutation

Euler's totient function, phi(n) [sometimes called the phi function], is defined 
  as the number of positive integers not exceeding n which are relatively prime 
  to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine 
  and relatively prime to nine, phi(9) = 6.
The number 1 is considered to be relatively prime to every positive number, so 
  phi(1) = 1.
Interestingly, phi(87109) = 79180, and it can be seen that 87109 is a 
  permutation of 79180.
Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and 
  the ratio n/phi(n) produces a minimum.
https://projecteuler.net/problem=70
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul
from common.iters import operate_list, permutation
from common.primes import tupled_prime_factors, prime_factors, prime_sieve

# --- Conditions of the problem ---
LIMIT = 10**7           # Exclusive


def phi(n: int) -> int:
    """Returns the totient / phi function value for number `n`."""
    paired_facs = tupled_prime_factors(n)
    return operate_list(1,[p**(i-1) * (p-1) for (p,i) in paired_facs],mul)


# --- Calculation ---
def main():
    best_ratio = 1000
    best_n = 1
    for n in range (2, LIMIT):
        pn = phi(n)

        # Update smallest perm ratio if necessary
        if permutation(str(n), str(pn)):
            ratio = n / pn
            if ratio < best_ratio:
                print("%s -> %s, %s -> %s" % (best_n, n, best_ratio, ratio))
                best_ratio = ratio
                best_n = n

    # Hypothesising it'll be better to work backwards from the limit to some 
    #   tipping point, rather than forwards
    

    # --- Output ---
    print(best_n)
    return
