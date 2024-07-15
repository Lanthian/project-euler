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


# --- Calculation ---
def main():
    not_lychrel = set()
    lychrel = set()

    # Work through ints in scoped range
    for i in range(1,LIMIT):
        # Skip numbers already categorized in other iterations
        if i in not_lychrel or i in lychrel: continue
        
        path = []
        i_s = str(i)
        x = False

        # Find lychrel / not lychrel chains beneath LIMIT
        while i < LIMIT:
            alt = int(i_s[::-1])
            path.append(i)
            # Add reverses together
            i += alt

            # Once again, skip already categorized numbers
            if i in lychrel: 
                lychrel.update(path)
                break
            elif i in not_lychrel:
                not_lychrel.update(path)
                break

            i_s = str(i)
            # If palindrome found, chain is not lychrel
            if palindrome(i_s):
                not_lychrel.update(path)
                break
            
        # Classify chain via looping 50 iterations deep
        else:
            for _ in range(ITERS-1):
                alt = int(i_s[::-1])
                path.append(i)
                # Add reverses together
                i += alt

                # Once again, skip already categorized numbers
                if i in lychrel: 
                    lychrel.update(path)
                    break
                elif i in not_lychrel:
                    not_lychrel.update(path)
                    break

                i_s = str(i)
                # If palindrome, every number up until this point is not lychrel
                if palindrome(i_s):
                    not_lychrel.update(path)
                    break
            # Otherwise, every number up until this point it lychreal
            else: lychrel.update(path)


    # --- Output ---
    print(len([l for l in lychrel if l < LIMIT])) # 249
    return
