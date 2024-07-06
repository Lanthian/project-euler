""" Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every odd composite number can be 
  written as the sum of a prime and twice a square.
    9 = 7 + 2 * 1^2
    15 = 7 + 2 * 2^2
    21 = 3 + 2 * 3^2
    25 = 7 + 2 * 3^2
    27 = 19 + 2 * 2^2
    33 = 31 + 2 * 1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime
  and twice a square?
https://projecteuler.net/problem=46
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import floor, sqrt
from common.primes import prime_generator


def goldbach_2(num: int, primes: set) -> bool:
    """Returns whether or not an odd composite number `num` supports 'Goldbachs 
    other conjecture', proven or disproven by generating this sum. Takes in a 
    set of `primes` that must span prime numbers up to num-2. Returns a boolean.
    """
    limit = floor(sqrt((num-3)//2))
    for i in range(1, limit+1):
        if (num - 2*i**2) in primes: return True
    return False


# --- Calculation & Output ---
def main():
    # Incrementally fill primes as necessary
    primes = set()

    prev = 2
    # Work through primes, finding odd composite numbers in between primes
    for p in prime_generator():
        primes.add(p)

        for comp in list(range(prev+2, p, 2)):
            # If a number fails goldbach's other conjecture, it is what we want
            if not goldbach_2(comp, primes): 
                print(comp) # 5,777
                return
        
        prev = p
