""" Magic 5-gon Ring

Consider the following "magic" 3-gon ring, filled with the number 1 to 6, and 
  each line adding to nine.
    <graph>
Working clockwise, and starting from the group of three with the numerically 
  lowest external node (4,3,2 in this exmaple), each solution can be described 
  uniquely. For example, the above solution can be described by the set: 4,3,2;
  6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11 and 
  12. There are eight solutions in total
    Total   Solution Set
    9       4,2,3; 5,3,1; 6,1,2
    9       4,3,2; 6,2,1; 5,1,3
    10      2,3,5; 4,5,1; 6,1,3
    10      2,5,3; 6,3,1; 4,1,5
    11      1,4,6; 3,6,2; 5,2,4
    11      1,6,4; 5,4,2; 3,2,6
    12      1,5,6; 2,6,4; 3,4,5
    12      1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum
  string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form
  16- and 17- digit strings. What is the maximum 16-digit string for a "magic" 
  5-gon ring?

https://projecteuler.net/problem=68
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.iters import ruled_perm_gen
from common.nums import charlist_to_int as t  # Aliased for shorthand

# --- Conditions of the problem ---
RING_SIZE = 5
TOTAL_SIZE = 2*RING_SIZE
NUMBERS = [str(e) for e in range(1,TOTAL_SIZE+1)]

SOUGHT_LENGTH = 16


def order_to_ring(seq: list, N: int) -> str:
    """Shorthand function to convert a permutation of elements that represent an
    N-gon ring (side length 3) into their full ring list."""
    # Append 2nd term to end of sequence (to reuse later in final side overlap)
    seq = list(seq) + [seq[1]]

    # Define first side, then build up remaining sides
    full = seq[:3]
    for side in range(1,N):
        full.extend([seq[2*side+1], full[-1], seq[2*(side+1)]])

    return full


# --- Calculation ---
def main():
    start = time.time()

    """Build permutations rules for N-gons with N > 2"""
    # Prepare additional early stage rules to prune permutations faster
    rules = {
        # length : [rules applicable up to (including) this length]
        4: [lambda x: str(int(x[0])+int(x[1])-int(x[3])) in NUMBERS]
    }
    # Add in N-gon loop requirements
    rules.update({
        i: [lambda x, i=i: int(x[i-4])+int(x[i-5]) == int(x[i-2])+int(x[i-1])] 
            for i in range(5,TOTAL_SIZE,2)
    })
    # Define unique magic N-gon loops by minimised starting value
    rules.update({
        i: [lambda x, i=i: int(x[0]) < int(x[i-1])] 
            for i in range(4,TOTAL_SIZE+1,2)
    })
    # Include final loop requirement (looping back to start)
    end = [lambda x: int(x[TOTAL_SIZE-3])+int(x[TOTAL_SIZE-4]) == 
        int(x[TOTAL_SIZE-1])+int(x[1])]
    if TOTAL_SIZE in rules: rules[TOTAL_SIZE].extend(end)
    else: rules[TOTAL_SIZE] = end

    max_ngon = 0
    for i in ruled_perm_gen(NUMBERS, rules):
        if not i: 
            print("No valid permutations discovered.")
            continue
        
        ngon = t(order_to_ring(i, RING_SIZE))
        # Update maximum SOUGHT_LENGTH digit ngon as necessary
        if SOUGHT_LENGTH is None or len(str(ngon)) == SOUGHT_LENGTH: 
            if ngon > max_ngon: max_ngon = ngon


    # --- Output ---
    print("Time:", time.time() - start)
    print(max_ngon) # 6531031914842725
    return
