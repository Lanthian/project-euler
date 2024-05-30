""" Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13->40->20->10->5->16->16->8->4->2->1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
  10 terms. Although it has not been proven yet (Collatz Problem), is it thought
  that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
https://projecteuler.net/problem=14
"""

__author__ = "Liam Anthian"

# --- Imports ---
from primes import factor

# --- Conditions of the problem ---
LIMIT = 1*10**6


def collatz_length(num: int, lengths: dict[int: int]) -> int:
    """Finds the collatz length of a number `num`. Recursively updates and 
    searches a dictionary of collatz numbers `lengths`."""
    # Base case (done in case 1 is not stored in dictionary already)
    if num == 1: return 1
    elif num in lengths: return lengths[num]

    elif factor(num, 2): new = num // 2
    else: new = 3*num + 1

    lengths[num] = collatz_length(new, lengths) + 1
    return lengths[num]


# --- Calculation ---
c_lengths = {1: 1}
max_length = 1
max_num = 1

for i in range(1, LIMIT):
    l = collatz_length(i, c_lengths)
    if l > max_length: 
        max_length = l
        max_num = i


# --- Output ---
print(max_num) # 837,799
