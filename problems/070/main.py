""" Totient Permutation

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


def phi_from_factors(n: int, primes: list[int]=[]) -> int:
    """Returns the totient / phi function value for number `n`."""
    paired_facs = tupled_prime_factors(n, primes)
    return operate_list(1,[p**(i-1) * (p-1) for (p,i) in paired_facs],mul)


# --- Calculation ---
def main():
    # # Generate primes in advance
    # primes = prime_sieve(LIMIT)
    #
    # best_ratio = 1000
    # best_n = 1
    # x = []
    # for n in range (2, LIMIT):
    #     pn = phi_from_factors(n, primes)
    #     x.append(pn)
    #
    #     # Update smallest perm ratio if necessary
    #     if permutation(str(n), str(pn)):
    #         ratio = n / pn
    #         if ratio < best_ratio:
    #             # print("%s -> %s (%s), %s -> %s" % (best_n, n, pn, best_ratio, ratio))
    #             best_ratio = ratio
    #             best_n = n

    # Hypothesising it'll be better to work backwards from the limit to some 
    #   tipping point, rather than forwards


    # -- New approach --
    """
    Algorithm learnt from: "https://stackoverflow.com/questions/34260399/ ...
      linear-time-eulers-totient-function-calculation" post, algo analysed by
      stack user DarthGizka - https://stackoverflow.com/users/4156577/

    Facts:  https://en.wikipedia.org/wiki/Euler%27s_totient_function
      * for prime p, φ(p) = p-1                     (euler's product formula)
      * for prime p, φ(p^k) = p^(k-1) * (p-1)       (φ of prime power argument)
      * for coprime x & p, φ(x*p) = φ(x) * φ(p)     (multiplicative function)
    φ(n) cases: 
      1. n is prime                         
            ->  φ(n) = n-1
      2. n = x*p, x & p coprime, p prime    
            ->  φ(n) = φ(x*p) = φ(x) * φ(p) = φ(x) * (p-1)
      3. n = x*p, x = x'*p^k, x' & p coprime, p prime 
            ->  φ(n) = φ(x) * p
    """

    # phi values 0 by default: prime until proven otherwise
    phi = [0] * LIMIT     
    primes = []

    # Answer variables
    best_ratio = 1000
    best_n = 1

    for n in range(2, LIMIT):
        # Case 1
        if phi[n] == 0: 
            phi[n] = n-1
            primes.append(n)

        # Prepare further cases 2 & 3 (sieve like)
        for p in primes:
            np = n * p
            # Check if out of search bounds
            if np >= LIMIT: break
            
            # Case 2 - coprime if remainder
            if n % p: phi[np] = phi[n] * (p-1)
            # Case 3 - not coprime since no remainder
            else: 
                phi[np] = phi[n] * p
                # Break to avoid repeating assignments
                break

        # Condition check - update smallest perm ratio if necessary
        if permutation(str(n), str(phi[n])):
            ratio = n / phi[n]
            if ratio < best_ratio:
                best_ratio = ratio
                best_n = n


    # --- Output ---
    print(best_n) # 8,319,823
    return
