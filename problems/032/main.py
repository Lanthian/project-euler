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


def singular(seq: str, whitelist: set=set(range(1,DIGITS))) -> bool:
    """Returns a boolean regarding if a string sequence `seq` has duplicate 
    characters in it - true if so, false otherwise. Whitelisted characters in 
    `whitelist` may validly appear multiple times."""
    filtered = [a for a in seq if a in whitelist]
    return list(dict.fromkeys(filtered)) == filtered


# --- Calculation ---
def main():
    pan_list = set()


    # Select multiplicand up the highest possible option
    for a in range(2, 10**((DIGITS-1)//2)):
        a_s = str(a)
        # Drop zeros
        if "0" in a_s: continue

        # Trim duplicate digits
        if not singular(a_s): continue

        # Select multiplier up to the highest possible option
        for b in range(2, 10**((DIGITS-len(a_s)-1))):
            b_s = str(b)
            # Drop zeros
            if "0" in b_s: continue

            # Trim duplicate digits
            flag = False
            if not singular(a_s+b_s): continue

            prod = a * b
            prod_s = str(prod)
            # Drop zeros
            if "0" in prod_s: continue

            if pandigital(a_s+b_s+prod_s, DIGITS):
                print(a, "*", b, "=", prod)
                # if flag: print(a_s+" * "+b_s+" = "+prod_s)
                pan_list.add(prod)

    # print(pandigital("953916872948", DIGITS))
        
    

    # print(pandigital("15234", 5))

    # --- Output ---
    print(sum(pan_list)) # 45,228
    return
