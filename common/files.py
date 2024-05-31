"""files.py: Functions for handling and creating files."""

__author__ = "Liam Anthian"

# --- Imports ---
from os.path import dirname, realpath, join


# First seen in 008 - Largest Product in a Series
def easy_open(file: str, target: str, mode: str = "r"):
    """Takes in current __file__ `file` of location called in, file to open 
    `target` and the `mode` of open - read by default."""
    # Find full directory of file
    directory = dirname(realpath(file))
    # Return opened file
    return open(join(directory, target), mode)
