""" Diophantine Equation

Consider quadratic Diophantine equations of the form:
    x^2 - D*y^2 = 1
For example, when D = 13, the minimal solution for x is 649^2 - 13 * 180^2 = 1.
It can be assumed that there are no solutions in positive integers where D is 
  square.
By finding minimal solutions in x for D = {2,3,5,6,7}, we obtain the following:
    3^2 - 2*2^2 = 1
    2^2 - 3*1^2 = 1
    9^2 - 5*4^2 = 1
    5^2 - 6*2^2 = 1
    8^2 - 7*3^2 = 1
Hence, by considering minimal solutions in x for D <= 7, the largest x is 
  obtained when D = 5.
Find the value of D <= 1000 in minimal solutions of x for which the largest 
  value of x is obtained.
https://projecteuler.net/problem=66
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import sqrt
from common.nums import int_gen, square_generator

# --- Conditions of the problem ---
LIMIT = 1000            # Inclusive


def int_root(num: int) -> int | None:
    """Returns the int root of a number `num` if it is a square number, returns 
    None if otherwise."""
    root = sqrt(num)
    as_int = int(root)
    if as_int == root: return as_int
    # Otherwise not a whole number, thus `num` is not square
    return False

def minimal_diophantine(d: int) -> tuple[int, int]:
    """Finds and returns the the minimum value of x in Diophantine equation 
    x^2 - `d`*y^2 = 1, minimised according to x."""
    for y2 in square_generator():
        x = int_root(1 + d*y2)
        # Only return if root is whole (1+d*y**2 is square)
        if x: return x


# --- Calculation ---
def main():
    greatest = 0
    sqrs = set()
    for d in range(2,LIMIT+1):
        # Track squares to skip later
        sqrs.add(d**2)
        # Check if this d needs skipping
        if d in sqrs: continue
        
        # Find x & y for this d
        x = minimal_diophantine(d)
        if x > greatest: 
            print("%s: %s -> %s" % (d, greatest,x))
            greatest = x
    

    # Benchmark for improvement
    # print(61, minimal_diophantine(61))
    
    # --- Output ---
    print(greatest)
    return


"""
2: 0 -> 3
5: 3 -> 9
10: 9 -> 19
13: 19 -> 649
29: 649 -> 9801
46: 9801 -> 24335
53: 24335 -> 66249
61: 66249 -> 335159612
109: 335159612 -> 372326272
151: 372326272 -> 498062163
199: 498062163 -> 640500731
271: 640500731 -> 667137236
331: 667137236 -> 770394803
461: 770394803 -> 959700061
517: 959700061 -> 1110550906
617: 1110550906 -> 1592796237
778: 1592796237 -> 2178548422
2178548422
Wrong?
"""