""" Amicable Chains

The proper divisors of a number are all the divisors excluding the number
  itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the 
  sum of these divisors is equal to 28, we call it a perfect number. 
Interestingly the sum of the proper divisors of 220 is 284 and the sum of the 
  proper divisors of 284 is 220, forming a chain of two numbers. For this 
  reason, 220 and 284 are called an amicable pair.
Perhaps less well known are longer chains. For example, starting with 12496, we 
  form a chain of five numbers:
    12496 -> 14288 -> 15472 -> 14536 -> 14264(-> 12496 -> ...)
Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding 
  one million

https://projecteuler.net/problem=95
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.primes import prime_sieve, proper_divisor_sum

# --- Conditions of the problem ---
LIMIT = 10**6
# Constants
PERFECT = 1
AMICABLE = 2
NOT_AMICABLE = 3


# --- Calculation ---
def main():
    start = time.time()

    # Filter out len(primes) numbers
    primes = set(prime_sieve(LIMIT))
    
    # Track seen numbers and longest chain
    seen = [0]*(LIMIT+1)
    longest_chain = []

    for n in range(2, LIMIT):
        # Skip primes - cannot be amicable
        if n in primes: 
            seen[n] = NOT_AMICABLE
            continue
        # Skip processing numbers already observed
        if seen[n]: continue

        s = proper_divisor_sum(n)
        # If amicably paired with self, "perfect number".
        if s == n: seen[n] = PERFECT
        else:
            chain = [n]
            while(s != chain[0]): 
                # Check for cycle failure, out of bounds, or chain collision
                if s == chain[-1] or s > LIMIT or seen[s]:
                    for i in chain: seen[i] = NOT_AMICABLE
                    break
                
                # Check for subchain success
                elif s in chain:
                    split = chain.index(s)
                    # Mark values prior to subchain as not amicable
                    for i in chain[:split]: seen[i] = NOT_AMICABLE

                    # Update current chain to subchain
                    chain = chain[split:]
                    # Skip chain 'step' in order to exit loop next iteration
                    continue

                # Take next chain step
                chain.append(s)
                s = proper_divisor_sum(s)
            
            # If s == chain[0], amicable chain!
            else: 
                for i in chain: seen[i] = AMICABLE
                if len(chain) > len(longest_chain):
                    longest_chain = chain

            
    # --- Output ---
    print("Time:", time.time() - start)
    print(min(longest_chain) if longest_chain else "No chain found.") # 14316
    return
