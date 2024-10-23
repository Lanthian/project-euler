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
    # 4,2,3; 5,3,1; 6,1,2
    rules = {
        # length : [rules applicable up to (including) this length]
        # Not needed, but the sooner we check, the more permutations pruned
        4:  [lambda x: str(int(x[0])+int(x[1])-int(x[3])) in NUMBERS], 
        5:  [lambda x: int(x[0])+int(x[1]) == int(x[3])+int(x[4])],
        7:  [lambda x: int(x[3])+int(x[2]) == int(x[5])+int(x[6])],
        9:  [lambda x: int(x[5])+int(x[4]) == int(x[7])+int(x[8])],
        11: [lambda x: int(x[7])+int(x[6]) == int(x[9])+int(x[10])],
    }

    # Include final loop
    final = [lambda x: int(x[TOTAL_SIZE-3])+int(x[TOTAL_SIZE-4]) == 
             int(x[TOTAL_SIZE-1])+int(x[1])]
    if TOTAL_SIZE in rules: rules[TOTAL_SIZE].extend(final)
    else: rules[TOTAL_SIZE] = final
        
    x = 0
    for i in ruled_perm_gen(NUMBERS, rules):
        if not i: continue
        print(t(i))
        x += 1
    print("matches", x)

    print(t(order_to_ring("423516", 3)))
    print(t(str(s) for s in order_to_ring(list(range(1,11)), 5)))
    print(t(str(s) for s in order_to_ring(['1','10','2','3','4','5','6','7','8','9'], 5)))

    # --- Output ---
    return
