""" Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous two 
  terms. By starting with 1 and 2, the first 10 terms will be:
    1,2,3,5,8,13,21,34,55,89
By considering the terms in the Fibonacci sequence whose values do not exceed 
  four million, find the sum of the even-valued terms.
https://projecteuler.net/problem=2
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
X0 = 1
X1 = 2
LIMIT = 4*10**6


def fibonacci(a1: int, a2: int, limit: int) -> list[int]:
    """Returns a list of all numbers less than `limit` in a fibonacci
    sequence starting at ints `a1` and `a2`. Recursive."""
    if a1 > limit: return []
    return [a1] + fibonacci(a2, a1+a2, limit)


# --- Output ---
sequence = fibonacci(X0,X1,LIMIT)
print(sum(filter(lambda x: x%2==0, sequence))) # 4,613,732
