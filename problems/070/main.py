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
from common.iters import permutation
from common.primes import prime_factors, prime_sieve

# --- Conditions of the problem ---
LIMIT = 10**7           # Exclusive


# --- Calculation ---
def main():
    primes = prime_sieve(LIMIT)
    prime_set = set(primes)
    not_prime = []
    
    factors = {}
    phi = {}
    
    best_ratio = 1000
    best_n = 1
    for n in range (2, LIMIT):
        factors[n] = set(prime_factors(n, primes, reduced=True))
        # If prime, don't need to check factor overlap
        if n in prime_set: phi[n] = n-1
       
        # Otherwise, count up relatively prime lower numbers
        else:
            count = 1
            for i in range(2,n):
    
                # Check if any factor overlap
                for factor in factors[n]:
                    if factor in factors[i]: break
                else: count += 1
            # And update phi(n) accordingly
            phi[n] = count

        # Update smallest perm ratio if necessary
        if permutation(str(n), str(phi[n])):
            ratio = n / phi[n]
            if ratio < best_ratio:
                print("%s -> %s, %s -> %s" % (best_n, n, best_ratio, ratio))
                best_ratio = ratio
                best_n = n

    # Hypothesising it'll be better to work backwards from the limit to some 
    #   tipping point, rather than forwards


    # --- Output ---
    print(best_n)
    return
