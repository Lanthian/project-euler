""" Names Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
  containing over five-thousand first names, begin by sorting it into 
  alphabetical order. Then working out the alphabetical value for each name, 
  multiply this value by its alphabetical position in the list to obtain a name 
  score.
For example, when the list is sorted into alphabetical order, COLIN, which is 
  worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain a 
  score of 938 x 53 = 49714.
What is the total of all the name scores in the file?
https://projecteuler.net/problem=22
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "0022_names.txt"
DELIM = ","


def value_word(word, zero=ord('A')-1) -> int:
    """Takes in any character iterable `word` and returns the sum of all it's 
    characters, treating `zero` as the base for 0 in character conversion.
    Takes '@' (A-1) as 0 by default."""
    return sum([ord(letter)-zero for letter in word])
    

# --- Calculation ---
def main():
    # Read in data
    names = [n.strip('"') for n in 
             easy_open(__file__, FILE, "r").readline().split(DELIM)]
    
    # Better sorting here would be ideal
    names.sort()


    # --- Output ---
    print(sum([i*value_word(n) for i,n in enumerate(names, 1)])) # 871,198,282
    return
