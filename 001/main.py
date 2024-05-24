""" Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
  3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
FACTORS = [3,5]
LIMIT = 1000


def find_products(factors: list[int], limit: int) -> set[int]:
    """Returns a set of all products containing any factors in list `factors` 
    that are below the cap `limit`."""
    products = set()

    for i in range(1, limit):        
        # Cut off range early if no new matches added
        cut_off = True

        # Store all unique multiplicants of 3 and 5
        for m in factors:
            v = m * i
            if v >= limit: continue
            cut_off = False
            products.add(v) 

    return products


# --- Output ---
print(sum(find_products(FACTORS, LIMIT))) # 233,168
