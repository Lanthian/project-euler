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
    
    total_longest = 0
    for i,p in enumerate(primes):
        total = p
        longest = 1
        for j in range(i+1, len(primes)):
            total += primes[j]
            if total in prime_set: longest = j-i
        
        if longest > total_longest: total_longest = longest


    # --- Output ---
    print(total_longest)
    return
