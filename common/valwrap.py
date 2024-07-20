"""valwrap.py: Provides a dataclass to wrap other datatypes with some numeric,
comparable value. Can be implemented stand alone from other files in module."""

__author__ = "Liam Anthian"

# Originally produced for:
#   COMP30024 Artificial Intelligence, Semester 1 2024
#   Project Part B: Single Player Tetress

from dataclasses import dataclass
from functools import total_ordering
from numbers import Number

@dataclass(slots=True)
@total_ordering
class ValWrap():
    """
    Storage of any datatype `item` alongside an int value `val` such that said 
    datatype can be compWared and sorted. Item may be None. 
    """
    val: Number
    item: ...

    def __eq__(self, other: 'ValWrap'):
        return self.val == other.val
    
    def __lt__(self, other: 'ValWrap'):
        return self.val < other.val
    
    def invert(self):
        self.val *= -1

    def increment(self):
        self.val += 1
    