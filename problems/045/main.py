""" Triangular, Pentagonal, and Hexagonal

Triangle, pentagonal, and hexagonal numbers are generated by the following 
  formulae:
    Triangle    Tn = n(n+1)/2   1,3,6,10,15,...
    Pentagonal  Pn = n(3n-1)/2  1,5,12,22,35,...
    Hexagonal   Hn = n(2n-1)    1,6,15,28,45,...
It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
https://projecteuler.net/problem=45
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import triangle, pentagonal, hexagonal 

# --- Conditions of the problem ---
GOAL = 2

# --- Constants ---
(N,KIND) = (0,1)


def ret(n: tuple[int,str], data: dict[str: tuple['function',dict[int,int]]]
        ) -> int:
    """Takes an index tuple `n` of index and index kind, and a dictionary
    `data` of conversion functions and converted values for these different 
    index kinds. Calculates and stores a new value if necessary for index before
    returning this value (int)."""
    # -- Constants --
    (FUNC,DATA) = (0,1)

    # Safety check that type exists
    if n[KIND] not in data: return -1

    elif n not in data[n[KIND]][DATA]: 
        # Populate data entry if missing
        data[n[KIND]][DATA][n[N]] = data[n[KIND]][FUNC](n[N])
    return data[n[KIND]][DATA][n[N]]


# --- Calculation ---
def main():

    data = {'t': (triangle,{}), 'p': (pentagonal,{}), 'h': (hexagonal,{})}
    def equal(ns: list[tuple[int,str]], data: dict) -> bool:
        """Helper function. Takes a list of tupled indices `ns` and using the 
        lookup/calculation function `ret`, returns a bool regarding if each
        n-shaped number is equal."""
        if len(ns) == 0: return True

        base = ret(ns[0], data)
        for n in ns[1:]:
            if ret(n,data) != base: return False
        # If all values equal, return true
        return True
    
    # Number of times they've lined up and tupled (index,type) for shape-nums
    hits = 0
    ns = [(1,'t'),(1,'p'),(1,'h')]

    # Loop through hits until desired match
    while (hits != GOAL):
        # If equal but not the correct hit number, step all forward
        if equal(ns,data): ns = [(n+1,t) for (n,t) in ns]

        # For each shaped number, cascade increase
        for i in range(len(ns)):
            # Increment this index of shaped number until >= other numbers
            other_max = max([ret(n,data) for n in ns[:i]+ns[i+1:]])
            while ret(ns[i],data) < other_max: ns[i] = (ns[i][N]+1,ns[i][KIND])

            # If they're all equal now, a new hit has been found
            if equal(ns, data): 
                hits += 1
                break


    # --- Output ---
    print(ret(ns[i],data)) # 1,533,776,805
    return
