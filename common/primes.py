"""primes.py: Functions for handling prime numbers - generation and checking."""

__author__ = "Liam Anthian"

# --- Imports ---
from math import sqrt


# First seen in 005 - Smallest Multiple
def factor(product: int, i: int) -> bool:
    """Returns True if `i` is a factor of `product`. False if otherwise."""
    return product % i == 0

# First seen in 012 - Highly Divisible Triangular Number
def factors(num: int) -> set[int]:
    """Returns a set of factors of `num`. Includes 1 and num."""
    fs = set()
    for i in range(1, num+1):
        # Only check up until sqrt(num) to reduce computation
        if i > sqrt(num): break
        if factor(num, i): 
            # In case of squareroot, only one instance added (benefit of set)
            fs.add(i)
            fs.add(num//i)
    return fs

# First seen in 026 - Reciprocal Cycles
def ordered_factors(num: int) -> list[int]:
    """Returns an ordered list of factors of `num`. Includes 1 and num."""
    front = []
    back = []
    root = sqrt(num)

    for i in range(1, num+1):
        # Only check up until sqrt(num) to reduce computation
        if i == root: 
            front.append(i)
            break
        elif i > root: break

        if factor(num, i): 
            front.append(i)
            back.insert(0, num//i)
    return front + back

# First seen in 021 - Amicable Numbers
def proper_divisor_sum(num: int) -> int:
    """Shorthand function to return the proper divisor sum of a number `num`."""
    return sum(factors(num).difference([num]))

# First seen in 003 - Largest Prime Factor
def prime(num: int, primes: list[int]) -> bool:
    """Checks if an int `num` is prime, according to possible factors in 
    `primes`. Returns a boolean."""
    # Break early if past last possible factor of num
    limit = sqrt(num)
    for p in primes:
        if p > limit: return True
        elif factor(num, p): return False
    return True

def is_prime(num: int) -> bool:
    """Checks if an int `num` is prime. Returns a boolean."""
    for prime in prime_generator():
        if prime > num: return False
        elif prime == num: return True

# First seen in 003 - Largest Prime Factor
def prime_generator():
    """A generator for prime numbers - uses `prime()` in prime construction."""
    yield 2
    yield 3
    primes = [2,3]

    i = 1
    while(True):
        # Generate primes via 6n-1, 6n+1
        for shift in [-1,1]:
            a = 6 * i + shift

            # Check if number is prime - yield if so
            if prime(a, primes):
                primes.append(a)
                yield a
        
        # Increment
        i += 1

# First seen in 003 - Largest Prime Factor
def prime_factors(product: int, primes: list[int]=[]) -> list[int]:
    """Takes a number `product` and finds and returns a list of all prime 
    factors that build it. Can take in a prior sufficiently large list of 
    `primes` instead of generating."""
    factors = []

    incrementor = primes if len(primes) > 0 else prime_generator()
    # Check if primes are factors of product
    for p in incrementor:
        while factor(product, p):
            # Store and remove factor from product
            factors.append(p)
            product = product//p

        # Check for cut off
        if p > product or product == 0: break
    return factors

# First seen in 047 - Largest Prime Factor
def powered_prime_factors(product: int, primes: list[int]=[]) -> list[int]:
    """Takes a number `product` and finds and returns a list of all fully 
    powered prime factors that build it. Can take in a prior sufficiently large 
    list of `primes` instead of generating."""
    factors = []

    incrementor = primes if len(primes) > 0 else prime_generator()
    # Check if primes are factors of product
    for p in incrementor:
        i = 0
        while factor(product, p):
            # Count and remove factor from product
            i += 1
            product = product//p
        if i > 0: factors.append(p ** i)

        # Check for cut off
        if p > product or product == 0: break
    return factors

# First seen in 010 - Summation of Primes
def prime_sieve(limit: int) -> list[int]:
    """Eratosthenes Sieve: Generates all primes up to `limit` (not inclusive) by 
    filtering out factors as it works up the range of possible primes."""
    # Shorthand functions for converting too and from array indexes to values
    def to_val(index: int) -> int:
        return 2*index+3
    def from_val(val: int) -> int:
        return (val-3)//2
    
    # Unsieved array
    length = from_val(limit+1)
    primes = [1]*length

    for i in range(0, length):
        # Skip factors that are combinations of smaller primes
        if primes[i] == 0: continue

        # If a prime, remove all greater composites
        val = to_val(i)

        if primes[i]: 
            for j in range(from_val(val**2), length, val):
                primes[j] = 0

    return [2] + [p*to_val(i) for i,p in enumerate(primes) if p]
