""" Convergents of e

The square root of two can be written as an infinite continued fraction.
    sqrt(2)=1+1/(2+1/(2+1/(2+1/(2+...))))
The infinite continued fraction can be written sqrt(2) = [1;(2)], (2) indicates
  that 2 repeats ad infinitum. In a similar way, sqrt(23)=[4;(1,3,1,8)].
It turns out that the sequence of partial values of continued fractions for 
  square roots provide the best rational approximations. Let us consider the
  convergents for sqrt(2).
    1 + 1/2 = 3/2
    1 + 1/(2+1/2) = 7/5
    1 + 1/(2+1/(2+1/2)) = 17/12
    1 + 1/(2+1/(2+1/(2+1/2))) = 41/29
Hence the sequence of the first ten convergents for sqrt(2) are:
    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant, e = 
  [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
The first ten terms in the sequence of convergents for e are:
    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7 = 17.
Find the sum of digits in the numerator of the 100th convergent of the continued
  fraction for e.
https://projecteuler.net/problem=65
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.fractions import Fraction, fr_add, fr_flip
from common.iters import operate_list
from common.nums import digit_sum

# --- Conditions of the problem ---
TERM = 100


def e_convergence_seq(index: int=0) -> int:
    """Takes an index `index` and returns the respective value in e's 
    convergence sequence. Assumes 0 to be the first index.
    Returns: 1,2,1,1,4,1,1,6,1,...,1,2k,1,...
    """
    if (index-1) % 3 == 0: return 2*(index+2)//3
    return 1


# --- Calculation ---
def main():
    # Variables for clarity sake
    zero = Fraction(0,1)
    two = Fraction(2,1)

    # E ad infinitum
    ls = [e_convergence_seq(i) for i in range(TERM-1)]

    # Find converging part of E fraction up to term TERM
    fr_converge = lambda base,y: fr_flip(fr_add(base, Fraction(y,1), 
                                                simplify=False))
    convergent_part = operate_list(zero, reversed(ls), fr_converge)
    # And find the overall numerator of this E representation
    numerator = fr_add(two, convergent_part, simplify=False).numer


    # # --- Output ---
    print(digit_sum(numerator)) # 272
    return
