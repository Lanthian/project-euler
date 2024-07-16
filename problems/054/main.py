""" Poker Hands

In the card game poker, a hand consists of five cards and are ranked, from 
  lowest to highest, in the following way:
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest 
  value wins; for example, a pair of eights beats a pair of fives (see example 1 
  below). But if two ranks tie, for example, both players have a pair of queens, 
  then highest cards in each hand are compared (see example 4 below); if the 
  highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:
    Hand    Player 1	 	    Player 2	 	        Winner
    1       5H 5C 6S 7S KD      2C 3S 8S 8D TD          Player 2
            Pair of Fives       Pair of Eights
    2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH          Player 1
            Highest card Ace    Highest card Queen
    3	 	2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
            Three Aces          Flush with Diamonds
    4	 	4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
            Pair of Queens      Pair of Queens
            Highest card Nine   Highest card Seven
    5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
            Full House          Full House
            With Three Fours    with Three Threes
The file, poker.txt, contains one-thousand random hands dealt to two players. 
  Each line of the file contains ten cards (separated by a single space): the 
  first five are Player 1's cards and the last five are Player 2's cards. You 
  can assume that all hands are valid (no invalid characters or repeated cards),
  each player's hand is in no specific order, and in each hand there is a clear 
  winner.
How many hands does Player 1 win?
https://projecteuler.net/problem=54
"""

__author__ = "Liam Anthian"

# --- Imports ---
from enum import Enum
from functools import total_ordering
from common.files import easy_open

# --- Conditions of the problem ---
FILE = 'poker.txt'
DELIM = ' '

@total_ordering
class Value:
    val: int

    conversion = {str(i):i for i in range(1,10)}
    conversion.update({"T":10, "J":11, "Q":12, "K":13, "A":14})

    def __init__(self, char: str) -> 'Value':
        self.val = self.conversion[char]

    def __str__(self) -> str:
        """Character representation of face value identifier."""
        for k,v in self.conversion.items():
            if v == self.val: return k
        # Return None if no match
        return None
    
    def __lt__(self, other: 'Value') -> bool:
        return self.val < other.val
    def __eq__(self, other: 'Value') -> bool:
        return self.val == other.val

class Suit(Enum):
    CLUB = "C"
    SPADE = "S"
    DIME = "D"
    HEART = "H"

    def read(char: str) -> 'Suit':
        """Equivalent to a __init__ but works with Enum"""
        for suit in Suit:
            if char == str(suit): return suit
        return None

    def __str__(self) -> str:
        """Character representation of suit identifier."""
        return str(self.value)
    
    def __eq__(self, other: 'Suit') -> bool:
        return str(self) == str(other)

@total_ordering
class Card:
    value: Value
    suit: Suit
    
    def __init__(self, text: str) -> 'Card':
        (VAL,SUIT) = (0,1)
        self.value = Value(text[VAL])
        self.suit = Suit.read(text[SUIT])

    def __str__(self) -> str: 
        return str(self.value)+str(self.suit)

    # Card suit is not used to determine if cards have equal value
    def __lt__(self, other: 'Card') -> bool:
        return self.value < other.value
    def __eq__(self, other: 'Card') -> bool:
        return self.value == other.value
    

# --- Calculation ---
def main():
    # Read in data
    # with easy_open(__file__, FILE) as fp:
    #     # print(fp.readlines())
    #     for game in fp.readlines():
    #         cards = game.strip('\n').split(DELIM)
    #     # print(fp.readline().split(DELIM))


    s = Suit.read("S")
    print(s)
    v = Value("K")
    print(v, v.val)

    c1 = Card("5D")
    c2 = Card("8H")
    c3 = Card("8D")
    
    print(c1, c2, c3)
    print(c1 < c2)
    print(c2 == c3)

    print(c1.suit == c2.suit)
    print(c1.suit == c3.suit)


    # --- Output ---
    return