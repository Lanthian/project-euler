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
import time
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "sudoku.txt"
SUDOKU_SIZE = 9
SQR_SIZE = 3

ROWS = "rows"
COLS = "col"
SQRS = "sqr"


def sqr(row: int, col: int) -> int:
    """Takes a row and column number for a sudoku coordinate (0,0 is top left).
    Returns the given square number in which this cell exists. For sudoku of 
    size 9, square numbers are as follows - [[0,1,2],[3,4,5],[6,7,8]]."""
    return SQR_SIZE*(row//SQR_SIZE) + col//SQR_SIZE

def solve_sudoku(sudoku: list[list[int]]) -> bool:
    """Takes a sudoku (2 dimensional square of size SUDOKU_SIZE) and solves it 
    in place. Returns True if successfully solved, False if otherwise. Assumes
    no faults exist in sudoku read in."""
    # Track the open values for each category of the sudoku
    options = {
        ROWS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)}, 
        COLS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)}, 
        SQRS: {k:set(range(1,SUDOKU_SIZE+1)) for k in range(SUDOKU_SIZE)}
    }

    # Track initially unsolved cells
    unsolved = []
    for row in range(SUDOKU_SIZE):
        for col in range(SUDOKU_SIZE):
            value = sudoku[row][col]
            # If unsolved cell, stop here (tracking it)
            if value == 0: unsolved.append((col,row)) # (x,y)
            
            # Otherwise remove solved value as options for relevant categories
            else:
                options[ROWS][row].discard(value)
                options[COLS][col].discard(value)
                options[SQRS][sqr(row,col)].discard(value)

    # Iterate over it until complete or no change
    while(len(unsolved)):
        prev = len(unsolved)

        # TODO - solving code
        for c,r in unsolved:
          print((c,r), "=", options[ROWS][r].union(options[COLS][c].union(options[SQRS][sqr(r,c)])))
          pass

        # No changes made in iteration, not solvable by this solver
        if len(unsolved) == prev: return False

    return True


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
            sudokus.append(sud)

    # Solve Sudokus
    for sudoku in sudokus:
      # x = sudoku[0][:3]
      # if not 0 in x: print(x)
      if solve_sudoku(sudoku):
        print(sudoku)
      exit(1)
            

    # --- Output ---
    print("Time:", time.time() - start)
    return
