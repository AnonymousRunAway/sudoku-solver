# Sudoku Solver
This Python script implements a Sudoku solver using a backtracking algorithm. It represents a Sudoku board as a 9x9 matrix of integers, where 0 represents an empty cell.

# Classes and Functions
## SudokuBoard:
Represents a Sudoku board with methods for checking row, column, and subgrid validity.
Provides a __str__ method for printing the board.
Implements the backtracking solver method to find a solution.
## solve_sudoku:
Creates a SudokuBoard instance and solves the given puzzle.
Prints the initial and solved puzzles.

# How it works
The SudokuBoard class creates a board object from a given 2D list.
The solver method recursively tries to fill empty cells with valid numbers.
If a valid number is found, it recursively calls itself to fill the next empty cell.
If no valid number is found, it backtracks and tries the next possible number in the previous cell.

# Usage
Create a 9x9 list representing the Sudoku puzzle, with 0 for empty cells.
Call the solve_sudoku function with the puzzle as input.
The function will print the initial and solved puzzles.

# Example
```python
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)
```
