""" Pandigital Fibonacci Ends

The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number 
  for which the last nine digits are 1-9 pandigital (contain all the digits 1 to
  9, but not necessarily in order). And F2749, which contains 575 digits, is the 
  first Fibonacci number for which the first nine digits are 1-9 pandigital.
Given that Fk is the first Fibonacci number for which the first nine digits AND 
  the last nine digits are 1-9 pandigital, find k.
https://projecteuler.net/problem=104
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.nums import fibonacci_generator, pandigital


# --- Calculation ---
def main():
    start = time.time()
    for i,x in enumerate(fibonacci_generator(),1):
        s = str(x)
        if pandigital(s[:9],9) and pandigital(s[-9:],9): break
    
    
    # --- Output ---
    print("Time:", time.time() - start)
    print(i,x)
    return
