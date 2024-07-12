""" Prime Digit Replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
  the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
  number is the first example having seven primes among the ten generated 
  numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
  56993. Consequently 56003, being the first member of this family, is the 
  smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily 
  adjacent digits) with the same digit, is part of an eight prime value family.
https://projecteuler.net/problem=51
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import permutation_generator, sublists
from common.primes import prime_sieve

# --- Conditions of the problem ---
FAMILY_SIZE = 8


def equal_index(num: str, indices: list[int]) -> bool:
    """Takes a number `num` in string form, checking if all `indices` specified 
    are equal. Ensure indices are a valid range before use. Indices do not need
    to be sorted. Returns this check as a boolean."""
    base = num[indices[0]]
    for i in indices[1:]:
        if num[i] != base: return False
    return True

def remove_index(word: str, indices: list[int]) -> str:
    """Takes a string `word` and removes characters at index locations specified
    in `indices`. Indices do not need to be sorted. Returns this new string."""
    i_set = set(indices)
    return "".join([char for i,char in enumerate(list(word)) if i not in i_set])


# --- Calculation ---
def main():
    digits = 0

    replacements = {}
    best = None
    # Incrementally increase digit count until answer found
    while(True):
        digits += 1

        # Prepare index replacement sublists - dropping empty and full set
        subs = sublists(list(range(digits)))[1:-1]

        # Generate primes of length 'digits'
        lower_bound = 10**(digits-1)-1
        primes = [p for p in prime_sieve(10**digits) if p > lower_bound]

        # Group primes by valid index replacements
        for indices in subs:
            i_s = "".join([str(i) for i in indices])
            # Reset dictionary each new index subset to free up space
            replacements.clear()

            for p in primes:
                p_s = str(p)

                # Check if valid index replacement here
                if equal_index(p_s, indices):
                    key = i_s+'.'+remove_index(p_s,indices)

                    # Create initial dict entry if unstored, and update counts        
                    if key not in replacements: replacements[key] = [0, p]
                    replacements[key][0] += 1

                    # Check if answer found - update new best if needed
                    if replacements[key][0] == FAMILY_SIZE: 
                        found = replacements[key][1]
                        # print(found, indices)
                        if best == None or found < best: best = found
                        # Move onto next index selection
                        break
        
        # If a match at this digit level has been found, return result
        if best != None: break


    # --- Output ---
    print(best) # 121,313
    return
