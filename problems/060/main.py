""" Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
  and concatenating them in any order the result will always be prime. For 
  example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
  primes, 792, represents the lowest sum for a set of four primes with this 
  property. 
Find the lowest sum for a set of five primes for which any two primes 
  concatenate to produce another prime.
https://projecteuler.net/problem=60
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import is_prime3 as is_prime, prime_generator 

# --- Conditions of the problem ---
FAMILY = 5


def paired(a: int, b: int) -> bool:
    """Returns True if numbers `a` and `b` are prime regardless of order of 
    concatenation. False if otherwise"""
    (a_s,b_s) = (str(a), str(b))
    if is_prime(int(a_s+b_s)) and is_prime(int(b_s+a_s)): return True
    return False

def expand_pair_set(value: int, pair_set: dict[int,dict]) -> list[int]:
    """Takes a recursive dictionary of pair set primes `pair_set` and attaches
    `value` onto valid sets of pairs. Returns longest retrievable pair set that
    includes `value`, in list form."""
    best = []
    for k,k_dict in pair_set.items():
        if paired(k, value): 
            new = [k] + expand_pair_set(value, k_dict)
            if len(new) > len(best): best = new
            k_dict[value] = {}
    
    if best == []: return [value]
    return best


# --- Calculation ---
def main():
    pair_sets = {}

    # Build up through primes
    for p in prime_generator():

        # Find longest pair set including p
        p_longest = expand_pair_set(p, pair_sets)
        if len(p_longest) == FAMILY: break

        # Create new 'set' of just p
        pair_sets[p] = {}
    

    # --- Output ---
    print(sum(p_longest)) # 26,033
