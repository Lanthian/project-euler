"""
https://projecteuler.net/problem=50
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import prime_sieve

# --- Conditions of the problem ---
LIMIT = 1000000         # Exclusive

# --- Calculation ---
def main():
    primes = prime_sieve(LIMIT)
    prime_set = set(primes)
    
    best_p = None
    longest = 0

    for i,p in enumerate(primes):
        total = p
        curr_best = p
        length = 1

        for j in range(i+1, len(primes)):
            total += primes[j]
            if total >= LIMIT: break

            # If summation up until this point is prime, new best for p found
            elif total in prime_set: 
                length = j-i+1
                curr_best = total
        
        # Update if new best found
        if length > longest: 
            longest = length
            best_p = curr_best


    # --- Output ---
    print(best_p) # 997,651
    return
