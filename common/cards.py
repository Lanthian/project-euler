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
    def __int__(self) -> int:
        return self.val
    
    def __lt__(self, other: 'Value') -> bool:
        return self.val < other.val
    def __eq__(self, other: 'Value') -> bool:
        if type(other) != type(self): return False
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
    def __int__(self) -> int:
        """Return card value as an integer."""
        return int(self.val)

    # Card suit is not used to determine if cards have equal value
    def __lt__(self, other: 'Card') -> bool:
        return int(self) < int(other)
    def __eq__(self, other: 'Card') -> bool:
        return int(self) == int(other)

@total_ordering
class Hand: 
    cards: list[Card]

    def __init__(self, cards: list[Card]) -> 'Hand':
        self.cards = cards
    # def __init__(self, cards: str, delim: str=" ") -> 'Hand':
    #     self.cards = [Card(s) for s in cards.split(delim)]

    def __str__(self, delim: str=" ") -> str:
        return delim.join([str(card) for card in self.cards])
    def __repr__(self) -> str:
        return "Hand(cards=%s)" % self.cards
    
    def rank(self):
        """Returns a list of comparable values, summarising how a hand scores.
        Assumes only 1 deck is in play (no 5 of a kind, or pairs within flushes)
        """
        MISS = None
        high = high_cards(self.cards)
        straight = straight_cards(self.cards, miss=MISS)

        # Check if flushed
        if flush_cards(self.cards):
            # 6: Regular flush
            if straight == MISS: return [6, high]
            # 9: Straight flush
            else: return [9, straight]

        # 5: Regular Straight
        elif straight != MISS: return [5, straight]
        
        # Check groupings
        groups = [(v,int(k)) for k,v in group_cards(self.cards).items()]
        groups.sort(reverse=True)

        if len(groups) == 2:
            # 8: 4 of a kind
            if groups[0][0] == 4: return [8, [v[1] for v in groups]]
            # 7: Full house
            else: return [7, [v[1] for v in groups]]
        
        elif len(groups) == 3: 
            # 4: 3 of a kind
            if groups[0][0] == 3: return [4, [v[1] for v in groups]]
            # 3: Two pair
            else: return [3, [v[1] for v in groups]]

        # 2: One pair
        elif len(groups) == 4: return [2, [v[1] for v in groups]]
        # 1: Just high card
        else: return [1, high]

    def __lt__(self, other: 'Card') -> bool:
        return self.rank() < other.rank()
    def __eq__(self, other: 'Card') -> bool:
        return self.rank() == other.rank()


def high_cards(cards: list[Card]) -> list[Value]:
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

def straight_cards(cards: list[Card], size:int=5, miss=None) -> Value:
    """Takes a list of Cards `cards` and returns the highest card Value if a
    straight of length `size` is present. Returns `miss` if otherwise."""
    top = max(cards)
    straight = list(range(int(top), int(top)-size,-1))
    # If straight decending from highest card == cards descending, success
    if straight == [int(c) for c in high_cards(cards)]:
        return top.val
    return miss


# --- Testing ---
"""
# P2 wins
h1_1 = Hand("5H 5C 6S 7S KD")
h1_2 = Hand("2C 3S 8S 8D TD")
print(max(h1_1, h1_2))

# P1 wins
h2_1 = Hand("5D 8C 9S JS AC")
h2_2 = Hand("2C 5C 7D 8S QH")
print(max(h2_1, h2_2))

# P2 wins
h3_1 = Hand("2D 9C AS AH AC")
h3_2 = Hand("3D 6D 7D TD QD")
print(max(h3_1, h3_2))

# P1 wins
h4_1 = Hand("4D 6S 9H QH QC")
h4_2 = Hand("3D 6D 7H QD QS")
print(max(h4_1, h4_2))

# P1 wins
h5_1 = Hand("2H 2D 4C 4D 4S")
h5_2 = Hand("3C 3D 3S 9S 9D")
print(max(h5_1, h5_2))
"""
