""" Su Doku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle 
  concept. Its origin is unclear, but credit must be attributed to Leonhard 
  Euler who invented a similar, and much more difficult, puzzle idea called 
  Latin Squares. The objective of Su Doku puzzles, however, is to replace the 
  blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 
  box contains each of the digits 1 to 9. Below is an example of a typical 
  starting puzzle grid and its solution grid.
    <graphic>
A well constructed Su Doku puzzle has a unique solution and can be solved by 
  logic, although it may be necessary to employ "guess and test" methods in 
  order to eliminate options (there is much contested opinion over this). The 
  complexity of the search determines the difficulty of the puzzle; the example 
  above is considered easy because it can be solved by straight forward direct 
  deduction.
The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), 
  contains fifty different Su Doku puzzles ranging in difficulty, but all with 
  unique solutions (the first puzzle in the file is the example above).
By solving all fifty puzzles find the sum of the 3-digit numbers found in the 
  top left corner of each solution grid; for example, 483 is the 3-digit number 
  found in the top left corner of the solution grid above.

https://projecteuler.net/problem=96
"""

__author__ = "Liam Anthian"

# --- Imports ---
from copy import deepcopy
import time
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "sudoku.txt"
SUDOKU_SIZE = 9
SQR_SIZE = 3

ROWS = "rows"
COLS = "cols"
SQRS = "sqrs"
COUNT = "count"


class Sudoku():
    # --- Initialisation ---
    def __init__(self, sudoku_grid: list[list[int]], 
                 patterns: tuple[dict[str: dict[int: list[int]]], 
                                 list[tuple[int,int]]] = None):
        """Takes a 2d grid `sudoku_grid` of dimensions SUDOKU_SIZE x SUDOKU_SIZE
        and stores it. Generates available pattern values (options) by default, 
        unless passed via `patterns` tuple (open_patterns, unsovled) - 
        reused if so."""
        # Deepcopy 2d array to avoid potential reuse
        self.grid = deepcopy(sudoku_grid)
        
        # Reuse options if given
        if patterns:
            self.open_patterns = deepcopy(patterns[0])
            self.unsolved = deepcopy(patterns[1])
        # Otherwise generate them fresh
        self.generate_options()
        return
    
    def generate_options(self):
        """Generates a dictionary `open_patterns` of available values for each 
        pattern present in the sudoku grid (rows, columns and squares). 
        Additionally generates and stores a list `unsolved` of all cells that 
        still need to be solved. 
        * `open_patterns`:  dict[str: dict[int: list[int]]]
        * `unsolved`:       list[tuple[int,int]]"""
        # Safety check that sudoku exists before checking for available options
        assert(self.grid)

        # Track the open values for each category of the sudoku
        self.open_patterns = {
            ROWS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)}, 
            COLS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)}, 
            SQRS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)},
            COUNT: {k:SUDOKU_SIZE for k in range(1,SUDOKU_SIZE+1)}
        }

        # Track initially unsolved cells
        self.unsolved = []
        for row in range(SUDOKU_SIZE):
            for col in range(SUDOKU_SIZE):
                value = self.grid[row][col]
                # If unsolved cell, track it
                if value == 0: self.unsolved.append((col,row)) # (x,y)
                
                # Otherwise remove value availability for relevant categories
                else: self.discard(value, row, col)


    # --- Available pattern retrieval & updating --- 
    def _patterns(self, row: int, col: int) -> list[set[int]]:
        """Returns a list of sets of available values for a cell (`col`,`row`) -
        aka grid[row][col]."""
        return [self.open_patterns[ROWS][row], 
                self.open_patterns[COLS][col],
                self.open_patterns[SQRS][Sudoku._sqr(row,col)]]

    def discard(self, value: int, row: int, col: int):
        """Removes a number `value` from the availability of all patterns 
        regarding cell (`col`,`row`)."""
        assert(self.open_patterns)
        for pattern in self._patterns(row,col): pattern.discard(value)
        # Decrease total available count of a value
        self.open_patterns[COUNT][value] -= 1

    def available(self, row: int, col: int) -> set[int]:
        """Returns a set of all available values for a cell (`col`,`row`)."""
        return set.intersection(*self._patterns(row,col))

    def _sqr(row: int, col: int) -> int:
        """Takes a row and column number for a sudoku coordinate (0,0 is top 
        left). Returns the given square number in which this cell exists. For 
        sudoku of size 9, square numbers are as follows:
            [[0,1,2],[3,4,5],[6,7,8]]."""
        return SQR_SIZE*(row//SQR_SIZE) + col//SQR_SIZE
    

    # --- Solve the Sudoku instance ---
    def solve(self) -> bool:
        """Takes a sudoku (2 dimensional square of size SUDOKU_SIZE) and solves 
        it recursively and in place. Returns True if successfully solved, False 
        if otherwise. Assumes no faults exist in sudoku read in. <br>
        Treats the Sudoku as a Constraint Satisfaction Problem."""
        # Base case
        if len(self.unsolved) == 0: return True

        # Select the most promising position in the grid to solve from
        # (Reduce branching via 'Most constraining variable')
        # TODO
        c,r = self.unsolved[0]
        
        # Recursively solve via backtracking - reduce branching via sorting on
        # (Leave flexibility via 'Least constraining value')
        # TODO
        for val in self.available(r,c):
            child = self.child(val,r,c)
            # Skip invalid moves
            if child == None: continue

            # If this action lead to success, update self
            if child.solve():
                self.grid = child.grid
                self.open_patterns = child.open_patterns
                self.unsolved.clear()
                return True
            # Otherwise, continue with to next possible value
    
        # If no solution from available values, impossible to solve this variant
        return False
    
    def make_action(self, value: int, row: int, col: int) -> bool:
        """Updates a Sudoku instance with a move played to a certain cell.
        Returns True if successful, False if an illegal move."""
        try:
            # Adds value to grid, removes unsolved cell, and updates patterns
            self.grid[row][col] = value
            self.unsolved.remove((col,row))
            for p in self._patterns(row, col): p.remove(value)
            # Decrease total available count of a value
            self.open_patterns[COUNT][value] -= 1
            return True
        
        # If move is invalid, an exception will be raised. Return False.
        except:
            print(f"Error: Illegal action selected - '{value}' to", 
                  f"{(col+1,row+1)} for \n{str(self).strip()}")
            return False
        
    def child(self, value: int, row: int, col: int) -> 'Sudoku':
        """Generates a deepcopy and then makes an action of placing `value` at
        coordinate (`col`,`row`). Returns this child Sudoku if succesful, None 
        if otherwise."""
        child_state = deepcopy(self)
        success = child_state.make_action(value, row, col)
        # If failed to make action return None
        return child_state if success else None
    

    # --- General methods ---
    def __str__(self) -> str:
        """Returns a Sudoku instance's grid as a multiline string."""
        line = "--" * (SUDOKU_SIZE+SQR_SIZE) + "- \n"
        
        out = line
        for r in range(SUDOKU_SIZE):
            out += "| "
            for c in range(SUDOKU_SIZE):
                out += f"{self.grid[r][c]} "
                if not (c+1)%SQR_SIZE: out += "| "
            out += "\n"
            if not (r+1)%SQR_SIZE: out += line
        return out


# --- Calculation ---
def main():
    start = time.time()
    
    # Read in sudokus from file
    sudokus = []
    with easy_open(__file__, FILE) as fp:
        # Count number of sudokus
        file_start = fp.tell()
        sudoku_no = len(fp.readlines()) // (1+SUDOKU_SIZE)
        fp.seek(file_start)

        for _ in range(sudoku_no):
            # Skip sudoku head
            fp.readline()
            # Read sudoku lines
            sud = [None]*SUDOKU_SIZE
            for row in range(SUDOKU_SIZE): 
                sud[row] = [int(c) for c in fp.readline().strip()]
            sudokus.append(Sudoku(sud))

    # Solve and sum Sudokus
    total = 0
    for sudoku in sudokus:
        if sudoku.solve():
            total += int("".join(str(c) for c in sudoku.grid[0][:3]))     
        else: 
            print(f"Error: Failed to solve Sudoku\n{str(sudoku).strip()}")

    # --- Output ---
    print("Time:", time.time() - start)
    print(total)
    return
