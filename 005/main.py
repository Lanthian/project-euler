""" Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 
  10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the 
  numbers from 1 to 20? 
https://projecteuler.net/problem=5
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul
from primes import prime_factors

# --- Conditions of the problem ---
RANGE = (1,20)          # inclusive


def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base

def count_dict(iterable) -> dict[...: int]:
    """Counts the number of occurences of each unique item in an iterable 
    `iterable`. Returns these counts in a dictionary."""
    counts = {}
    for i in iterable:
        if i not in counts: counts[i] = 0
        counts[i] += 1
    return counts


# --- Calculation ---
factor_count = {}

# Find the total needed count of each factor
for i in range(RANGE[-1], RANGE[0]-1, -1):

    # Iterate over counted prime factor frequency of number `i`
    for f,count in count_dict(prime_factors(i)).items():
        # Track newly seen factor, or update if new greater count needed
        if f not in factor_count or count>factor_count[f]:
            factor_count[f] = count

product = operate_list(1, [k**v for k,v in factor_count.items()], mul)

# # Check divisible
# for i in range(RANGE[0], RANGE[1]+1):
#     print(f"ans / {i} -> {product/i}")


# --- Output ---
print(product) # 232,792,560 
