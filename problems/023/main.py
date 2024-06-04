""" Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly 
  equal to the number. For example, the sum of the proper divisors of 28 
  would be 1+2+4+7+14=28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
  n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that 
  can be written as the sum of two abundant numbers is 24. By mathematical 
  analysis, it can be shown that all integers greater than 28123 can be written 
  as the sum of two abundant numbers. However, this upper limit cannot be 
  reduced any further by analysis even though it is known that the greatest 
  number that cannot be expressed as the sum of two abundant numbers is less 
  than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
  two abundant numbers.
https://projecteuler.net/problem=23
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import proper_divisor_sum

# --- Conditions of the problem ---
LIMIT = 28123


def abundant(num: int) -> bool:
    """Returns a boolean regarding if a number is abundant or not; if the sum of 
    its proper divisors is greater than itself."""
    return proper_divisor_sum(num) > num


# --- Calculation ---
def main():
    # Find all abundant numbers below LIMIT
    ab_nums = [_ for _ in range(1,LIMIT) if abundant(_)]
    ab_set = set(ab_nums)
    
    total = 0 
    # Iterate over each number below abundant sum limit - O(LIMIT^2)
    for n in range(1, LIMIT):
        for ab in ab_nums:
            # Add number to total if no other abundant addends sum to n
            if n < 2*ab: 
                total += n
                break

            # Skip number if abundant addend present
            if n-ab in ab_set: break


    # --- Output ---
    print(total) # 4,179,871
    return
