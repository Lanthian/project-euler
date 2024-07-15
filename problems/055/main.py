""" Lychrel Numbers

If we take 47, reverse and add, 47+74=121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
    349 + 943 = 1292
    1292 + 2921 = 4213
    4213 + 3214 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, 
  never produce a palindrome. A number that never forms a palindrome through the
  reverse and add process is called a Lychrel number. Due to the theoretical 
  nature of these numbers, and for the purpose of this problem, we shall assume
  that a number is Lychrel until proven otherwise. In addition you are given 
  that for every number below ten-thousand, it will either (i) become a 
  palindrome in less than fifty iterations, or, (ii) no one, with all the 
  computing power that exists, has managed so far to map it to a palindrome. In 
  fact, 10677 is the first number to be shown to require over fifty iterations 
  before producing a palindrome: 4668731596684224866951378664 (53 iterations, 
  28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
  the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
NOTE: Wording was modified slightly on 24 April 2007 to emphasise the 
  theoretical nature of Lychrel numbers.
https://projecteuler.net/problem=55
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import palindrome

# --- Conditions of the problem ---
LIMIT = 10000           # Exclusive
ITERS = 50


def is_lychrel(x: int, loops: int=50) -> bool:
    """Iterates through 'x + x reversed ?= palindrome' lychral process for
    `loops` many iterations. Returns False if number `x` is not lychrel, and 
    True if number is lychral within loops testing bound."""
    x_s = str(x)
    path = []
    for _ in range(loops):
        # Add reverses together
        path.append(x)
        x += int(x_s[::-1])
        x_s = str(x)

        if palindrome(x_s):
            # (Every non-reversed number up until this point also isn't Lychrel)
            return False
        
    # Otherwise, every number up until this point is Lychrel (based on loops).
    return True

def lychrel_step(cur: int, lych: set[int]=set(), not_lych: set[int]=set(), 
                 path: list[int]=[]) -> bool | int:
        """Performs 1 step of lychrel processing of a given `path`, with known
        lychrel `lych` and non-lychrel `not_lych` numbers. Updates findings in
        these number sets, returning True (bool) if processing is done at end of
        time of calling, current number (int) next in chain if otherwise."""
        path.append(cur)
        # Add reverses together
        cur += int(str(cur)[::-1])

        # Skip already categorized numbers, categorizing chain so far
        if cur in lych: 
            lych.update(path)
        elif cur in not_lych:
            not_lych.update(path)

        # If palindrome found, chain is not Lychrel
        elif palindrome(str(cur)):
            not_lych.update(path)
  
        # Returns cur and continues if none of the above apply. Otherwise, True.
        else: return cur
        return True


# --- Calculation ---
def main():
    not_lychrel = set()
    lychrel = set()

    # Work through ints in scoped range
    for i in range(1,LIMIT):
        # Skip numbers already categorized in other iterations
        if i in not_lychrel or i in lychrel: continue

        path = []
        # Boolean flag to measure if chain is determinably not lychrel
        not_done = True

        # Find Lychrel / not Lychrel chains beneath LIMIT
        while not_done and i < LIMIT:
            i = lychrel_step(i, lychrel, not_lychrel, path)
            if i == True: not_done = False
            
        # Classify chain via looping ITERS iterations deep
        if not_done:
            for _ in range(ITERS-1):
                i = lychrel_step(i, lychrel, not_lychrel, path)
                if i == True: 
                    not_done = False
                    break
            # Otherwise, every number up until this point is a Lychrel number
            if not_done: lychrel.update(path)


    # --- Output ---
    print(len([l for l in lychrel if l < LIMIT])) # 249
    # print(len([x for x in range(1,LIMIT) if is_lychrel(x)])) # 249
    return
