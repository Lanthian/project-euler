"""nums.py: Miscellaneous functions for handling number problems."""

__author__ = "Liam Anthian"


# First seen in 027 - Quadratic Primes
def int_gen(start: int):
    """A generator for increasing integer numbers - starts at `start` (incls)"""
    while(True):
        yield start
        start += 1

# First seen in 030 - Digit Fifth Powers
def find_cap(digit_cost: int) -> int:
    """Taking `digit_cost` as the maximum cost of a digit in a linear problem, 
    finds and returns the int value at which no greater solutions will be found.
    """
    x = 0
    while(digit_cost * x >= 10**x - 1): x+=1
    return(digit_cost * x)

# First seen in 032 - Pandigital Products
def pandigital(seq: str, n: int, strict: bool=True, start: int=1) -> bool:
    """Returns if a string sequence `seq` is n-pandigital or not as a boolean. 
    Pandigital if digits `start` through to `n` inclusive are present once and 
    only once in `seq`. Boolean `strict` can be set to enforce that ONLY digits
    in range are present."""
    RANGE = [str(n) for n in range(start, n+1)]

    # If strict, only allow singular digits in the above range
    if strict:
        seen = set()

        if len(seq) != len(RANGE): return False

        # Check characters in sequence
        for d in seq:
            # If already observed or invalid, return false
            if d in seen or d not in RANGE: return False
            seen.add(d)
        return True

    # Otherwise allow digits and characters outside of range
    else:
        seen = {}

        # Count characters in sequence
        for d in seq:
            if d not in seen: seen[d] = 0
            seen[d] += 1

        # Check digit frequency
        for x in RANGE:
            if x not in seen: return False
            elif seen[x] != 1: return False
        
    return True
