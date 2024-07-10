""" Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
  one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, 
  contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most 
  consecutive primes?
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

    # Loop through all prime slices
    for i,p in enumerate(primes):
        # Primes over half of limit won't sum to anything less than limit
        if p > LIMIT // 2: break

        # Trackers / initial values
        total = p
        curr_best = total
        length = 1

        # Sum with greater primes to try and find a later consec-sum-prime
        for j in range(i+1, len(primes)):
            total += primes[j]
            # A total greater than limit is a stopping point
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
