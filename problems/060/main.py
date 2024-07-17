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
FAMILY = 4


def paired(a: int, b: int) -> bool:
    """Returns True if numbers `a` and `b` are prime regardless of order of 
    concatenation. False if otherwise"""
    (a_s,b_s) = (str(a), str(b))
    if is_prime(int(a_s+b_s)) and is_prime(int(b_s+a_s)): return True
    return False


# --- Calculation & Output ---
def main():
    pair_sets = []

    # Build up through primes
    for p in prime_generator():
        # Try including new prime in each existing pair set
        for p_set in pair_sets:
            # If matches, track new longer pair set
            # if all([paired(p,x) for x in p_set]): 
            for x in p_set:
                if not paired(p,x): break
            else:
                new = p_set.union({p})
                pair_sets.append(new)

                # Terminating point
                if len(new) == FAMILY: 
                    print(sum(new)) # 26,033
                    return

        pair_sets.append({p})
        # print(pair_sets)
