""" Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one 
  possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
  are listed numerically or alphabetically, we call it lexicographic order. The 
  lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
  6, 7, 8 and 9?
https://projecteuler.net/problem=24
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial

# --- Conditions of the problem ---
PATTERN = "0123456789"
NUMBER = 10**6


def permutation_generator(order: str, sep: str=''):
    """A generator for permutations of characters in the string `order`. Joins 
    characters together with `sep` connector."""
    # Loop through each possible head of permutation level
    for i,item in enumerate(order):
        rest = order[:i] + order[i+1:]

        # Base case (last item in iterable)
        if len(rest) == 0: yield item
        
        # Otherwise recursively attach on next set of permutations
        else: 
            for i_next in permutation_generator(rest, sep):
                yield sep.join([item, i_next])


def permutation_selection(order: str, number: int, validity_check: bool=True
                          ) -> str | None:
    """Takes a sequence in the form `order` and returns the nth (`number`) 
    permutation of the sequence. Checks if the selection bounds are valid if 
    `validity_check` flag is set to true. Leave this flag True by default."""
    length = len(order)

    if validity_check:
        # Make sure selected permutation is not less than start
        if 0 > number-1: return None
        # Check if selection is greater than number of permutations present
        elif factorial(length) < number-1: return None

    # Terminating point
    if length == 1: return order

    # Stepping size of each permutation at this depth in string
    step = factorial(length-1)
    
    for i,k in enumerate(order):
        # Check if selected permutation is in this slice
        if step > number-1: 
            remaining = order[:i]+order[i+1:]
            return k + permutation_selection(remaining, number)
        # Otherwise step permutation size `step` closer to selection
        else: number -= step

    return "ERROR: Incomplete Validation"


# --- Calculation & Output ---
def main():
    # # Loop through all permutations until chosen permutation reached
    # for i,perm in enumerate(permutation_generator(PATTERN), 1):
    #     if i != NUMBER: continue
    #
    #     # Number reached - output permutation
    #     print(perm) # 2,783,915,460
    #     break

    print(permutation_selection(PATTERN, NUMBER)) # 2,783,915,460
