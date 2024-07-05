""" Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive 
  integers:
    0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the 
  following expression.
    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
https://projecteuler.net/problem=40
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul
from common.iters import operate_list as op_list
from common.nums import int_gen

# --- Conditions of the problem ---
SELECTION = [1, 10, 100, 1000, 10000, 100000, 1000000]


def champernowne(n: int) -> str:
    """Generates the decimal places of champernowne's constant up to place `n`.
    Returns decimal places as a string."""
    out = ""
    for i in int_gen(1):
        if len(out) >= n: return out[:n]
        else: out += str(i)

def champernowne_digit(n: int) -> int:
    """Finds the `n`th digit of Champernowne's constant. Formula discovered via
    Stavros Panagiotidis' following youtube video: 
    https://www.youtube.com/watch?v=skbSd0yn-1g&ab_channel=StavrosPanagiotidis
    """
    # -- Proof of concept --
    # if n < 10:
    #     return int(str(1 + (n-1)//1)[((n)%2)-1])
    # elif n < 190:
    #     return int(str(10 + (n-9-1)//2)[((n-9)%2)-1])
    # elif n < 2890:
    #     return int(str(100 + (n-189-1)//3)[(n-189)%3-1])
    # else: return -1

    def num_of(x: int) -> int: 
        """Sub function. Returns the index distance of numbers up to length `x` 
        into Champernowne's constant."""
        return sum([(9*10**(i-1)) * i for i in range(1,x+1)])

    # Iterate through possible necessary distances into Champernowne constant
    for i in int_gen(1):
        cap = num_of(i)
        if n < cap+1:
            # Find starting point of numbers of length i in Champernowne string
            distance_in = n-num_of(i-1)

            # Find number at `n` pos in champernowne string
            number = 10**(i-1) + (distance_in-1) // i
            # Find specific index of above number visible at `n`
            index = (distance_in % i)-1
            # Combine number and index to find digit present at `n`
            return int(str(number)[index])


# --- Calculation ---
def main():
    # prod = 1
    # selection_set = set(SELECTION)
    # for i,v in enumerate(champernowne(SELECTION[-1]),1):
    #     if i in selection_set: prod *= int(v)
    

    # --- Output ---
    # print(prod) # 210

    
    # --- Further Research ---
    print(op_list(1, [champernowne_digit(i) for i in SELECTION], mul)) # 210
    return
