"""iters.py: Functions for handling and operating across iterables."""

__author__ = "Liam Anthian"


# First seen in 005 - Smallest Multiple
def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base

# First seen in 030 - Digit Fifth Powers
def find_cap(digit_cost: int) -> int:
    """Taking `digit_cost` as the maximum cost of a digit in a linear problem, 
    finds and returns the int value at which no greater solutions will be found.
    """
    x = 0
    while(digit_cost * x >= 10**x - 1): x+=1
    return(digit_cost * x)
