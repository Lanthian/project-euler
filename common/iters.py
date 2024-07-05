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
def ruled_perm_gen(order: str, rules: dict[int,list['function']]={}, 
                   prefix: str='', sep: str=''):
    """A generator for permutations of characters in the string `order`. Joins 
    characters together with `sep` connector. Recursively passes previous 
    items down through `cur` to check the properties `rules` against - trimming
    any permutations which break any rules."""

    def check_rules(state: str, rules: dict) -> bool:
            """Helper function for `ruled_perm_gen`. By length, checks if 
            `state` (current permutation prefix as a string) passes all boolean 
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

    # Loop through each possible head of permutation level. If no possible
    #   children can be generated, yield false
    any_valid = False
    for i,item in enumerate(order):
        if not check_rules(prefix+item, rules): continue

        rest = order[:i] + order[i+1:]
        # Base case (last item in iterable)
        if len(rest) == 0: yield item
        
        # Otherwise recursively attach on next set of permutations
        else: 
            for suffix in ruled_perm_gen(rest, rules, prefix+item, sep):
                # Toggle flag if valid perm path found
                if suffix == False: continue
                else: any_valid = True

                yield sep.join([item, suffix])
    
    # No possible children means this permutation branch needs to be terminated
    if not any_valid: yield False
