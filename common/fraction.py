"""fraction.py: Class for handling and utilising functions."""

__author__ = "Liam Anthian"

# --- Import --- 
from common.primes import ordered_factors, factor


# First seen in 057 - Square Root Convergents
class Fraction():
    numer: int
    denom: int

    def __init__(self, numer: int, denom: int) -> 'Fraction':
        self.numer = numer
        self.denom = denom 
    # def __init__(self, combined: str) -> 'Fraction':
    #     sep = combined.split("/")
    #     self.numer = int(sep[0])
    #     self.denom = int(sep[1])
    # def __init__(self, decimal: float, places: int=10**8) -> 'Fraction':
    #     """Converts an easy decimal `decimal` with less than `places` decimal 
    #     places to a Fraction type."""
    #     self.numer = int(decimal*places)
    #     self.denom = places
    #     self.simplify()

    def __str__(self) -> str:
        return "%s/%s" % (self.numer, self.denom)
    def __repr__(self) -> str:
        return "Fraction(numer=%s, denom=%s)" % (self.numer, self.denom)

    def __float__(self) -> float:
        """Evaluates fraction as a float."""
        return self.numer / self.denom
    def __round__(self, digits = None) -> float:
        return round(self.numer/self.denom, digits)
    def __int__(self) -> int:
        return int(self.numer / self.denom)
    def remainder(self) -> 'Fraction':
        return Fraction(self.numer%self.denom, self.denom)
    
    def add(self, other: 'Fraction', simplify: bool = True):
        """Adds another fraction to itself."""
        self.numer = self.numer*other.denom + other.numer*self.denom
        self.denom = self.denom*other.denom
        if simplify: self.simplify()

    def mul(self, other: 'Fraction', simplify: bool = True):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        if simplify: self.simplify()

    def simplify(self):
        """Simplifies itself to smallest form."""
        # Find greatest common factor (GCF) to divide by
        for f in reversed(ordered_factors(self.numer)):
            if factor(self.denom,f):
                self.numer = self.numer//f
                self.denom = self.denom//f
                return
