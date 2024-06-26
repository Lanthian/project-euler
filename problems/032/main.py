""" Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the 
  digits 1 to n exactly one; for example, the 5-digit number, 15234, is 1 
  through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing 
  multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can 
  be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only 
  include it once in your sum.
https://projecteuler.net/problem=32
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
DIGITS = 9


def pandigital(seq: str, n: int, start: int=1) -> bool:
    """Returns if a string sequence `seq` is n-pandigital or not as a boolean. 
    Pandigital if digits `start` through to `n` inclusive are present once and 
    only once in `seq`."""
    seen = {}

    # Count characters in sequence
    for d in seq:
        if d not in seen: seen[d] = 0
        seen[d] += 1

    # Check digit frequency
    for x in range(start, n+1):
        c = str(x)
        if c not in seen: return False
        elif seen[c] != 1: return False
    
    return True

def singular(seq: str, whitelist: set=set()) -> bool:
    """Returns a boolean regarding if a string sequence `seq` has duplicate 
    characters in it - true if so, false otherwise. All characters not
    whitelisted in `whitelist` may validly appear multiple times. Whitelist
    ignored by default."""
    if len(whitelist) == 0: filtered = seq
    else: filtered = [a for a in seq if a in whitelist]
    return list(dict.fromkeys(filtered)) == filtered


# --- Calculation ---
def main():
    pan_list = set()
    whitelist = set(range(1,DIGITS+1))

    # Select multiplicand up the highest possible option
    max_a = 10**((DIGITS-1)//2)
    for a in range(2, max_a):
        a_s = str(a)
        # Drop zeros
        if "0" in a_s: continue
        # Trim duplicate digits
        elif not singular(a_s, whitelist): continue

        # Select multiplier up to the highest possible option
        max_b = 10**((DIGITS-1)//2 - len(a_s) + 1)
        for b in range(2, max_b):
            b_s = str(b)
            # Drop zeros
            if "0" in b_s: continue
            # Trim duplicate digits
            elif not singular(a_s+b_s, whitelist): continue

            # Logic regarding product calculation
            prod = a * b
            prod_s = str(prod)
            # Drop zeros
            if "0" in prod_s: continue
            # Trim too large products
            elif len(prod_s) != len(a_s) + len(b_s) - 1: continue

            # Check and store pandigitals
            elif pandigital(a_s+b_s+prod_s, DIGITS):
                # print(a, "*", b, "=", prod)
                pan_list.add(prod)


    # --- Output ---
    print(sum(pan_list)) # 45,228
    return
