""" Totient Maximum

Euler's totient function, phi(n) [sometimes called the phi function], is defined 
  as the number of positive integers not exceeding n which are relatively prime 
  to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine 
  and relatively prime to nine, phi(9) = 6.
    <table>
It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.
Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
https://projecteuler.net/problem=69
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_factors, prime_generator, prime_sieve 

# --- Conditions of the problem ---
LIMIT = 10**6           # Inclusive


# --- Calculation ---
def main():
    # primes = prime_sieve(LIMIT)
    # prime_set = set(primes)
    # not_prime = []
    #
    # factors = {}
    # phi = {}
    #
    # best_n_div_phi = 1
    # best_n = 1
    # for n in range (2, LIMIT+1):
    #     factors[n] = set(prime_factors(n, primes, reduced=True))
    #     # If prime, don't need to check factor overlap
    #     if n in prime_set: phi[n] = n-1
    #    
    #     # Otherwise, count up relatively prime lower numbers
    #     else:
    #         count = 1
    #         for i in range(2,n):
    #
    #             # Check if any factor overlap
    #             for factor in factors[n]:
    #                 if factor in factors[i]: break
    #             else: count += 1
    #         # And update phi(n) accordingly
    #         phi[n] = count
    #        
    #     # Update greatest n/phi(n)
    #     n_div_phi = n / phi[n]
    #     if n_div_phi > best_n_div_phi:
    #         print("%s -> %s, %s -> %s" % (best_n, n, best_n_div_phi, n_div_phi))
    #         best_n_div_phi = n_div_phi
    #         best_n = n

    # Greatest n/phi(n) will be maximised when it is the multiplicand of the
    #   most primes; can quickly find best by just multiplying primes < LIMIT
    best = 1
    for p in prime_generator():
        next_best = best * p
        if next_best < LIMIT: best = next_best
        else: break


    # --- Output ---
    # print(best_n)
    print(best) # 510,510
    return
