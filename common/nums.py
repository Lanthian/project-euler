"""nums.py: Miscellaneous functions for handling number problems."""

__author__ = "Liam Anthian"


# First seen in 030 - Digit Fifth Powers
def find_cap(digit_cost: int) -> int:
    """Taking `digit_cost` as the maximum cost of a digit in a linear problem, 
    finds and returns the int value at which no greater solutions will be found.
    """
    x = 0
    while(digit_cost * x >= 10**x - 1): x+=1
    return(digit_cost * x)

# First seen in 032 - Pandigital Products
def pandigital(seq: str, n: int, start: int=1) -> bool:
    """Returns if a string sequence `seq` is n-pandigital or not as a boolean. 
    Pandigital if digits `start` through to `n` inclusive are present once and 
    only once in `seq`."""
    seen = {}

    # Count characters in sequence
    for d in seq:
        if d not in seen: seen[d] = 0
        seen[d] += 1

    # Check digit frequency
    for x in range(start, n+1):
        c = str(x)
        if c not in seen: return False
        elif seen[c] != 1: return False
    
    return True
