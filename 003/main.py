""" Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
https://projecteuler.net/problem=3
"""

__author__ = "Liam Anthian"

# Conditions of the problem
PRODUCT = 600851475143


def prime(num: int, primes: list[int]) -> bool:
    """Checks if an int `num` is prime, according to possible factors in 
    `primes`. Returns a boolean."""
    for i in primes:
        if num % i == 0: return False
    return True

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

def prime_factors(product: int) -> list[int]:
    """Takes a number `product` and finds and returns a list of all prime 
    factors that build it."""
    factors = []

    # Incrementally generate primes and check if they are factors of product
    for p in prime_generator():
        if product % p == 0:
            # Store and remove factor from product
            factors.append(p)
            product = product//p

        # Check for cut off
        if p > product or product == 0: break
    return factors


# Output
print(prime_factors(PRODUCT)[-1]) # 6,857
