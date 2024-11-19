""" Darts

In the game of darts a player throws three darts at a target board which is 
  split into twenty equal sized sections numbered one to twenty.
    <dart board graphic>
The score of a dart is determined by the number of the region that the dart 
  lands in. A dart landing outside the red/green outer ring scores zero. The 
  black and cream regions inside this ring represent single scores. However, the
  red/green outer ring and middle ring score double and treble scores 
  respectively.
At the centre of the board are two concentric circles called the bull region, or 
  bulls-eye. The outer bull is worth 25 points and the inner bull is a double, 
  worth 50 points.
There are many variations of rules but in the most popular game the players will 
  begin with a score 301 or 501 and the first player to reduce their running 
  total to zero is a winner. However, it is normal to play a "doubles out" 
  system, which means that the player must land a double (including the double 
  bulls-eye at the centre of the board) on their final dart to win; any other 
  dart that would reduce their running total to one or lower means the score for 
  that set of three darts is "bust".
When a player is able to finish on their current score it is called a "checkout" 
  and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).
There are exactly eleven distinct ways to checkout on a score of 6:
    D3		
    D1	D2	
    S2	D2	
    D2	D1	
    S4	D1	
    S1	S1	D2
    S1	T1	D1
    S1	S3	D1
    D1	D1	D1
    D1	S2	D1
    S2	S2	D1
Note that D1 D2 is considered different to D2 D1 as they finish on different 
  doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.
In addition we shall not include misses in considering combinations; for 
  example, D3 is the same as 0 D3 and 0 0 D3.
Incredibly there are 42336 distinct ways of checking out in total.
How many distinct ways can a player checkout with a score less than 100?

https://projecteuler.net/problem=109
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from enum import Enum
from functools import total_ordering
from common.iters import ruled_combo_gen

# --- Conditions of the problem ---
DARTS = 3
LIMIT = 100

class DartMult(Enum):
    SINGLE = 1
    DOUBLE = 2
    TREBLE = 3
        
@total_ordering
class DartRegion():
    def __init__(self, number: int, multiplier: int):
        # Will ValueError if given an invalid multiplier
        self.num = number
        self.mult = DartMult(multiplier)

    def __int__(self):
        return self.num*self.mult.value
    def __str__(self):
        return f"{(self.mult.name)[0]}{self.num}"
    def __repr__(self):
        return str(self)  # f"DartRegion(num={self.num},mult={self.mult})"
    
    def __lt__(self, other):
        return int(self) < int(other)
    def __eq__(self, other):
        return int(self) == int(other)

    # Functions for adding DartRegions simply (for use in sum())
    def __radd__(self, other):
        if other == 0: return self
        else: return self.__add__(other)
    def __add__(self, val):
        return int(self)+int(val)


# --- Calculation ---
def main():
    start = time.time()

    # Default regions, multiplied regions, and bullseyes
    regions = [DartRegion(n,m) for n in range(1,21) for m in range(1,4)]
    regions.extend([DartRegion(25,m) for m in range(1,3)])

    total = 0
    # Work through each possible checkout value and count distinct combinations
    for checkout in range(1,171):
        if checkout == LIMIT: break

        # Simple rules for generation
        rules = {i: [lambda x, y=checkout: sum(x) <= y] for i in range(1,DARTS)}
        rules[DARTS] = [lambda x, y=checkout: sum(x) == y]

        valid = []
        for combo in ruled_combo_gen(regions, DARTS, rules=rules):
            # If no valid combinations, pass
            if not combo: break
            # If valid checkout combination, add to list
            elif combo[-1].mult == DartMult.DOUBLE and sum(combo) == checkout: 
                valid.append(combo)
                
        total += len(valid)


    # --- Output ---
    print("Time:", time.time() - start)
    print(total)
    return
