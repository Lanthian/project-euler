"""countset.py: Class for handling and utilising custom CountSet class."""

__author__ = "Liam Anthian"


class CountSet():
    """Custom set built from a dictionary with keys=items, values=counts."""
    items: dict[...: int]

    def __init__(self, iterable: iter=[]):
        self.items = {}
        self.update(iterable)

    def __str__(self) -> str:
        return str(self.items)
    
    def __iter__(self) -> iter:
        """Converts set to iter object."""
        return iter(sum([[k]*count for k,count in self.items.items()],[]))


    def __contains__(self, item: ...):
        """Returns if a value `item` is in a CountSet."""
        return item in self.items
    
    def remove(self, item: ...):
        """Raises an error if item is not in CountSet."""
        self.items[item] -= 1
        if self.items[item] == 0: del self.items[item]

    def discard(self, item: ...):
        """Does not raise an error if item is not in CountSet."""
        if item in self.items: self.remove(item)

    def add(self, item: ...):
        """Adds an item into self.items, incrementing count if necessary."""
        # Increment item count if second+ occurence
        if item in self.items: self.items[item] += 1
        # otherwise Initialise item if first occurence
        else: self.items[item] = 1

    def update(self, iterable: iter):
        """Adds items from `iterable` into self.items, incrementing the counts 
        of already existing instances."""
        for item in iterable: self.add(item)
            

    def __eq__(self, other: object) -> bool:
        """Returns if another object `other` equals CountSet."""
        if isinstance(other, CountSet): return self.items == other.items
        elif isinstance(other, dict): return self.items == other
        elif isinstance(other, list): return list(self) == other
        elif isinstance(other, set): 
            # Make sure all counts == 1, otherwise not set convertible
            for v in self.items.values(): 
                if v != 1: return False
            return set(self) == other
        # Remaining cases
        else: self == other
