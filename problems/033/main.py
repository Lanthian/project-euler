""" Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
  attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
  correct, is obtained by cancelling the 9s.
We shall consider fractions like 30/50=3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than
  one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find
  the value of the denominator.
https://projecteuler.net/problem=33
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import factor, ordered_factors

# --- Conditions of the problem ---
LIMIT = 4


def num_append(nums: list[int]) -> int:
    """Front to back conjoins ints in list `nums` together. Returns this int."""
    return int("".join([str(n) for n in nums]))

def reduce(fraction: tuple[int, int]) -> tuple[int, int]:
    """Reduces a `fraction` represented as a tuple to smallest equivalent
    form. Returns this reduction as a tuple of numerator and denominator."""
    # Unpack fraction
    (numer, denom) = fraction
    # Find greatest common factor (GCF) to divide by
    for f in reversed(ordered_factors(numer)):
        if factor(denom,f): return (numer//f, denom//f)


# --- Calculation ---
def main():
    simplified = []

    # Loop through simplified numerators and denominators, skipping zeroes
    for numer in range(1,10):
        # denom >= numer
        for denom in range(numer+1,10):

            # Range selected as so, since fractions must be < 1
            for common in range(denom+1,10):
                # Append cancelled digit to numbers
                num_2 = num_append([numer,common])
                den_2 = num_append([common,denom])

                # Store and track these digit cancelling fractions
                if num_2/den_2 == numer/denom:
                    # print(num_2, "/", den_2)
                    simplified.append((numer,denom))


    # --- Output ---
    prod = (1,1)
    for (n,d) in simplified:
        prod = (prod[0] * n, prod[1] * d)
    print(reduce(prod)[1]) # 100    
    return
