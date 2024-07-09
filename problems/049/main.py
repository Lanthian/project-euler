""" Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
  by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
  (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
  exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this 
  sequence?
https://projecteuler.net/problem=49
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import permutation
from common.primes import prime_sieve

# --- Conditions of the problem ---
DIFFERENCE = 3330
DIGITS = 4


# --- Calculation ---
def main():
    start = 10**(DIGITS-1)  # inclusive
    end = 10**DIGITS        # exclusive

    primes = prime_sieve(end)
    # Trim primes start
    for i,p in enumerate(primes):
        if p >= start: break
    primes = primes[i:]
    primes_set = set(primes)

    # Trim primes end
    for j,p in enumerate(primes):
        if p + DIFFERENCE * 2 > end -1: break
    primes = primes[:j]
    
    matches = []

    # 1st
    for p in primes:
        p_s = str(p)

        # 2nd
        n1_p = p + DIFFERENCE
        n1_s = str(n1_p)
        if n1_p in primes_set and permutation(p_s, n1_s):
            
            # 3rd
            n2_p = n1_p + DIFFERENCE
            n2_s = str(n2_p)
            if n2_p in primes_set and permutation(p_s, n2_s):
                
                # Match found
                matches.append(p_s+n1_s+n2_s)
    
    
    # --- Output ---
    print(matches[1]) # 296,962,999,629
    return
