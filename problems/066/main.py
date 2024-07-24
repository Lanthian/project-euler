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
from common.nums import int_gen

# --- Conditions of the problem ---
LIMIT = 1000            # Inclusive


def minimal_diophantine(d: int) -> tuple[int, int]:
    """Finds and returns the the minimum value of (x,y) in Diophantine equation 
    x^2 - `d`*y^2 = 1, minimised according to x."""
    for y in int_gen(1):
        # d_y2 = x**2 - 1
        # if d_y2 % d != 0: continue
        # y = sqrt(d_y2//d)
        # # Check if y is a whole number (y^2 is a valid square)
        # if y % 1 == 0: return (x,int(y))

        x2 = 1 + d*y**2
        x = sqrt(x2)
        # Check if y is a whole number (y^2 is a valid square)
        if x % 1 == 0: return (x,int(y))



# --- Calculation ---
def main():
    greatest = 0
    sqrs = set()
    # for d in range(2,LIMIT+1):
    #     # Track squares to skip later
    #     sqrs.add(d**2)
    #     # Check if this d needs skipping
    #     if d in sqrs: continue
        
    #     # Find x & y for this d
    #     (x,_) = minimal_diophantine(d)
    #     if x > greatest: 
    #         print("%s: %s -> %s" % (d, greatest,x))
    #         greatest = x
    

    print(61, minimal_diophantine(61))
    
    # --- Output ---
    print(greatest)
    return
