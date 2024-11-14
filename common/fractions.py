"""fractions.py: Class for handling and utilising fractions."""

__author__ = "Liam Anthian"

# --- Import --- 
from functools import total_ordering
from common.primes import ordered_factors, factor


# First seen in 057 - Square Root Convergents
@total_ordering
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
        """Returns the a new fraction instance of just the fraction portion of a 
        potentially composite fraction."""
        return Fraction(self.numer%self.denom, self.denom)
    
    def add(self, other: 'Fraction', simplify: bool = True):
        """Adds another fraction to itself. Simplifies fraction if `simplify` 
        flag set to True."""
        self.numer = self.numer*other.denom + other.numer*self.denom
        self.denom = self.denom*other.denom
        if simplify: self.simplify()

    def mul(self, other: 'Fraction', simplify: bool = True):
        """Multiplies itself by another fraction. Simplifies fraction if 
        `simplify` flag set to True."""
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        if simplify: self.simplify()

    def invert(self):
        """Inverts itself - switching numerator and denominator."""
        temp = self.numer
        self.numer = self.denom
        self.denom = temp

    def simplify(self):
        """Simplifies itself to smallest form."""
        # Find greatest common factor (GCF) to divide by
        for f in reversed(ordered_factors(self.numer)):
            if factor(self.denom,f):
                self.numer = self.numer//f
                self.denom = self.denom//f
                return
    
    def __lt__(self, other: 'Fraction') -> bool:
        return self.numer*other.denom < other.numer*self.denom
    def __eq__(self, other: 'Fraction') -> bool:
        if type(other) != type(self): return False
        return self.numer*other.denom == other.numer*self.denom
    
    def __hash__(self):
        return hash(str(self))
    
    # BROKEN - commented out
    # def __getitem__(self, indices):
    #     """Allows retrieving Fraction instance numerator and denominator via 
    #     [x] notation. Doesn't handle multiple negative indices."""
    #     # Convert indices into a tuple if necessary
    #     if not isinstance(indices, tuple):
    #         indices = tuple(indices)

    #     # Numerator - 0, Denominator - 1, Error - everything else
    #     parts = [self.numer, self.denom]
    #     if len(indices) == 1: return parts[indices[0]]
        
    #     # Unexpected but allowed multiple indices (for slicing, for example)
    #     else: 
    #         out = []
    #         for i in indices:
    #             if i in [0,1]: out += parts[i]
    #         return out      


# First seen in 057 - Square Root Convergents
def fr_add(a: 'Fraction', b: 'Fraction', simplify: bool = True) -> 'Fraction':
    """Adds two fractions together and returns their result as a new instance. 
    Simplifies fraction if `simplify` flag set to True."""
    f =  Fraction(a.numer*b.denom + b.numer*a.denom, a.denom*b.denom)
    if simplify: f.simplify()
    return f

# First seen in 057 - Square Root Convergents
def fr_flip(a: 'Fraction') -> 'Fraction':
    """Inverts a fraction, returning a new instance.."""
    return Fraction(a.denom,a.numer)
