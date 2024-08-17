class SudokuBoard:
    def __init__(self, board: list[list[int]]) -> None:
        self._board = board
    
    def __str__(self) -> str:
        board_str = ''
        for row in self._board:
            board_str += ' '.join([str(i) if i else '*' for i in row]) + '\n'
        return board_str
    
    def _isValidRow(self, num: int, row: int) -> bool:
        return num not in self._board[row]

    def _isValidColumn(self, num: int, column: int) -> bool:
        return all(self._board[row][column] != num for row in range(9))

    def _isValid3x3(self, num: int, row: int, column: int) -> bool:
        row_start = (row // 3) * 3
        col_start = (column // 3) * 3
        return all(
            self._board[r][c] != num
            for r in range(row_start, row_start + 3)
            for c in range(col_start, col_start + 3)
        )

    def _is_valid(self, row: int, col: int, num: int) -> bool:
        return (
            self._isValidRow(num, row) and
            self._isValidColumn(num, col) and
            self._isValid3x3(num, row, col)
        )

    def _findEmptyCell(self):
        for row in range(len(self._board)):
            if 0 in self._board[row]:
                return (row, self._board[row].index(0))
        return None
    
    def solver(self) -> bool:
        if (next_empty := self._findEmptyCell()) is None:
            return True
        for guess in range(1, 10):
            if self._is_valid(next_empty[0], next_empty[1], guess):
                row, col = next_empty
                self._board[row][col] = guess
                if self.solver():
                    return True
                self._board[row][col] = 0
        return False
    

def solve_sudoku(board: list[list[int]]) -> SudokuBoard:
    gameboard = SudokuBoard(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

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