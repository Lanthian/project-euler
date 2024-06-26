"""iters.py: Functions for handling and operating across iterables."""

__author__ = "Liam Anthian"


# First seen in 004 - Largest Palindrome Product
def palindrome(iterable) -> bool:
    """Returns a boolean for if an iterable `iterable` is palindromic or not. 
    Works on strings, arrays, tuples - any discrete iterables."""
    # Compare front to back
    for i in range(len(iterable)//2):
        if iterable[i] == iterable[-(i+1)]: continue
        
        # If not palindromic, return false
        else: return False
    return True

# First seen in 005 - Smallest Multiple
def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base

# First seen in 024 - Lexicographic Permutations
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
