""" Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, tn = 1/2 * n(n+1);
  so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its 
  alphabetical position and adding these values we form a word value. For 
  example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
  is a triangle number then we shall call the word a triangle word.
Using <words.txt>, a 16K text file containing nearly two-thousand common English
  words, how many are triangle words?
https://projecteuler.net/problem=42
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.files import easy_open
from common.nums import triangle_generator, value_word

# --- Conditions of the problem ---
FILE = 'words.txt'
DELIM = ','
QUOTE = '"'

MAX_ESTIMATE = 45*26


# --- Calculation ---
def main():
    # Prepare triangle numbers
    triangles = set()
    for i in triangle_generator():
        if i > MAX_ESTIMATE: break
        triangles.add(i)

    # Read in data
    with easy_open(__file__, FILE) as fp:

        # For each word in file, check if word is a triangle coded
        count = 0
        for word in fp.readline().split(DELIM):
            # If indeed triangular, add to tally
            if (value_word(word.strip(QUOTE)) in triangles): count += 1
    

    # --- Output ---
    print(count) # 162
    return
