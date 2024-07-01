""" Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, 
  {a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
https://projecteuler.net/problem=39
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
LIMIT = 1000            # Inclusive


def triangles(perimeter: int) -> list[tuple]:
    """Find all possible pythagorean triples for a given `perimeter` (a+b+c). 
    Return this triples as a list of tuples."""
    out = []

    for a in range(1, perimeter//3):
        for b in range(a+1, (perimeter-a)//2):
            c = perimeter-a-b
            # If pythagorean triplet, store for output and exit this search lvl
            if a**2 + b**2 == c**2: 
                out.append((a,b,c))
                break
    
    return out


# --- Calculation ---
def main():
    best = None
    best_length = 0

    for i in range(12, LIMIT+1):
        trs = len(triangles(i))
        # Update new best
        if trs > best_length:
            best = i
            best_length = trs


    # --- Output ---
    print(best) # 840
    return
