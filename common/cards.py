"""cards.py: Class for handling and operating across cards."""

__author__ = "Liam Anthian"

# --- Imports ---
from enum import Enum
from functools import total_ordering


# First seen in 054 - Poker Hands
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
    def __repr__(self) -> str:
        return "Value(val=%s)" % self.val
    
    def __lt__(self, other: 'Value') -> bool:
        return self.val < other.val
    def __eq__(self, other: 'Value') -> bool:
        return self.val == other.val
    
    def __hash__(self) -> int:
        return hash(self.val)

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
    val: Value
    suit: Suit
    
    def __init__(self, text: str) -> 'Card':
        (VAL,SUIT) = (0,1)
        self.val = Value(text[VAL])
        self.suit = Suit.read(text[SUIT])

    def __str__(self) -> str: 
        return str(self.val)+str(self.suit)
    def __repr__(self) -> str:
        return "Card(value=%s, suit=%s)" % (repr(self.val), repr(self.suit))

    # Card suit is not used to determine if cards have equal value
    def __lt__(self, other: 'Card') -> bool:
        return self.val < other.val
    def __eq__(self, other: 'Card') -> bool:
        return self.val == other.val

# @total_ordering
class Hand: 
    cards: list[Card]

    def __init__(self, cards: list[Card]) -> 'Hand':
        self.cards = cards

    def __str__(self, delim: str=" ") -> str:
        return delim.join([str(card) for card in self.cards])
    def __repr__(self) -> str:
        return "Hand(cards=%s)" % self.cards

    def high_card(cards: list[Card]) -> list[Value]:
        """Takes a list of Cards `cards` and returns a list of descending card
        values."""
        # Base case - empty hand
        if cards == []: return []

        # Otherwise sort by descending card value
        cards.sort(reverse=True)
        return [card.val for card in cards]
    
    def group_cards(cards: list[Card]) -> dict[Value,int]:
        """Takes a list of Cards `cards` and returns a dictionary of card value
        counts."""
        seen = {}
        for c in cards:
            if c.val not in seen: seen[c.val] = 0
            seen[c.val] += 1
        return seen
    
    def flush_cards(cards: list[Card]) -> bool:
        """Takes a list of Cards `cards` and returns a boolean of if cards are 
        flushed (all same suit) or not."""
        # Here we have defined empty lists as flushed.
        if len(cards) == 0: return True
        base = cards[0].suit
        for c in cards[1:]:
            if c.suit != base: return False
        return True
