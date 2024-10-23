"""files.py: Functions for handling and creating files."""

__author__ = "Liam Anthian"

# --- Imports ---
from os import getcwd, makedirs, path


# First seen in 008 - Largest Product in a Series
def easy_open(file: str, target: str, mode: str = "r"):
    """Takes in current __file__ `file` of location called in, file to open 
    `target` and the `mode` of open - read by default."""
    # Find full directory of file
    directory = path.dirname(path.realpath(file))
    # Return opened file
    return open(path.join(directory, target), mode)

def make_problem(num: int): 
    """Generate new problem folder for problem `num` with __main__.py and 
    main.py files."""
    # Make directory if non-existant
    folder = path.join(getcwd(), "problems", "{:03d}".format(num))
    if not path.exists(folder):
        makedirs(folder)

    # Make main.py file if non-existant
    file1 = path.join(folder, "main.py")
    if not path.exists(file1):
        fp = open(file1, "w")
        fp.write(f'"""\nhttps://projecteuler.net/problem={num}\n"""\n')
        fp.write('\n__author__ = "Liam Anthian"\n')
        fp.write('\n# --- Imports ---\n')
        fp.write('\nimport time\n')
        fp.write('\n# --- Conditions of the problem ---\n')
        fp.write('\n\n# --- Calculation ---\n')
        fp.write('def main():\n')
        fp.write('    start = time.time()\n')
        fp.write('    # --- Output ---\n')
        fp.write('    print("Time:", time.time() - start)\n')
        fp.write('    return\n')

    # Make __main__.py file if non-existant
    file2 = path.join(folder, "__main__.py")
    if not path.exists(file2):
        fp = open(file2, "w")
        fp.write('# Project Euler: https://github.com/Lanthian/project-euler\n')
        fp.write('\nfrom .main import main\n')
        fp.write('\nif __name__ == "__main__":\n')
        fp.write('    main()\n')

    return
