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


def triangles(p: int) -> list[tuple]:
    """Find all possible pythagorean triples for a given perimeter `p` (a+b+c). 
    Return this triples as a list of tuples."""
    out = []

    for a in range(1, p//3):
        # Using perimeter and pythagorean triplet rule, see if b is whole number
        b = p*(p-2*a) / (2*(p-a))
        if b.is_integer():
            b = int(b)
            out.append((a,b,p-a-b))
    
    return out


# --- Calculation ---
def main():
    best = None
    best_length = 0

    for i in range(12, LIMIT+1, 2):
        trs = len(triangles(i))
        # Update new best
        if trs > best_length:
            best = i
            best_length = trs


    # --- Output ---
    print(best) # 840
    return


    # --- Further Research ---
    """User rayfil notes on the projecteuler thread the following -
      From a^2+b^2=c^2 and the ruling (odd^2 = odd, even^2 = even):
        * If a,b are even, c is even -> P is thus even (3*even)
        * If a,b are odd, c is even (odd+odd) -> P is thus even (2*odd+even)
        * If a even, b odd, c is odd (odd+even) -> P is thus even (2*odd+even)
      Thus P need only be checked for even numbers.

      From a^2+b^2=c^2 and a+b+c=P: 
        a^2 + b^2 = (P-a-b)^2
        a^2 + b^2 = P^2 + a^2 + b^2 - 2aP - 2bP + 2ab
        0 = P^2 - 2aP - 2bP + 2ab
        2bP - 2ab = P^2 - 2aP
        2b(P-a) = P(P-2a)
        b = P(P-2a) / 2(P-a)
      If b is whole, c (a+b) is whole and a pythagorean triplet is found.
    """