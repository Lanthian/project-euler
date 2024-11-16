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

# First seen in 043 - Sub-string Divisibility
def _check_rules(state: list, rules: dict) -> bool:
    """Helper function for `ruled_perm_gen` and `ruled_combo_gen`. By length, 
    checks if `state` (current combo prefix as a list) passes all boolean 
    functions `rules` at related depth/length. Returns a boolean."""
    # Current length
    cur = len(state)

    # Check rules at current depth/length
    if cur in rules:
        for rl in rules[cur]:
            # If a rule is not passed, state is invalid
            if not rl(state): return False

    # Otherwise, all rules passed -> true!
    return True

# First seen in 043 - Sub-string Divisibility
def ruled_perm_gen(order: list, rules: dict[int,list['function']]={}, 
                   prefix: list=[]):
    """A generator for permutations of elements in the list `order`. Recursively 
    passes previous items down through `cur` to check the properties `rules` 
    against - trimming any permutations which break any rules."""
    # Loop through each possible head of permutation level. If no possible
    #   children can be generated, yield false
    any_valid = False
    for i,item in enumerate(order):
        if not _check_rules(prefix+[item], rules): continue

        rest = order[:i] + order[i+1:]
        # Base case (last item in iterable)
        if len(rest) == 0: yield [item]
        
        # Otherwise recursively attach on next set of permutations
        else: 
            for suffix in ruled_perm_gen(rest, rules, prefix+[item]):
                # Toggle flag if valid perm path found
                if suffix == False: continue
                else: any_valid = True

                yield [item] + suffix
    
    # No possible children means this permutation branch needs to be terminated
    if not any_valid: yield False

# First seen in 113 - Non-bouncy Numbers
def ruled_combo_gen(order: list, length: int, 
                    rules: dict[int,list['function']]={}, prefix: list=[], 
                    fixed_length: bool=False):
    """A generator for combinations of elements in the list `order`. Recursively 
    passes previous items down through `cur` to check the properties `rules` 
    against - trimming any combinations which break any rules. Only returns 
    combinations at max length `length` if `fixed_length` flag set to true."""
    # If no possible combination additions, flag end by returning False
    if length == 0: 
        yield False
        return

    # Loop through each possible head of permutation level. If no possible
    #   children can be generated, yield false
    any_valid = False
    for i,item in enumerate(order):
        if not _check_rules(prefix+[item], rules): continue
        
        # Yield valid combination if not fixed
        if not fixed_length: yield [item]

        # Base case if fixed
        if fixed_length and length == 1: yield [item]
        
        # Otherwise, yield valid combinations then recursively attach on next 
        # possible combination suffixes.
        else: 
            for suffix in ruled_combo_gen(order, length-1, rules, prefix+[item]):
                # Toggle flag if valid perm path found
                if suffix == False: continue
                else: any_valid = True

                yield [item] + suffix
    
    # No possible children means this combination branch needs to be terminated
    if not any_valid: yield False

# First seen in 049 - Prime Permutations
def permutation(a, b) -> bool:
    """Takes two iterables `a` and `b` and returns if they are permutations of 
    each other (boolean)."""
    if len(a) != len(b): return False

    # Convert b to list form if necessary
    b = list(b)

    # Iterate through elements in a
    for a_c in a:
        # Try and match them with an element in b
        for i,b_c in enumerate(b):
            if a_c == b_c: break

        # If no match, not a permutation
        else: return False
        # otherwise, drop matched element
        b = b[:i] + b[i+1:]

    return True

# First seen in 051 - Prime Digit Replacements
def sublists(ite: list) -> list:
    """Takes a list `ite` and returns a list of the subsets of its items. 
    Includes the full set and empty set []."""
    subs = []

    # Base cases
    if len(ite) == 1: return [ite, []]
    elif ite == []: return [[]]         # sublist(s) of [] is []

    # Recursive cases
    s2 = sublists(ite[1:]) 
    subs += [[ite[0]]+s for s in s2]
    subs += s2

    return subs
