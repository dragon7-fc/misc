37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

* Each of the digits `1-9` must occur exactly once in each row.
* Each of the digits `1-9` must occur exactly once in each column.
* Each of the the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

Empty cells are indicated by the character `'.'`.

![37_250px-Sudoku-by-L2G-20050714.svg.png](img/37_250px-Sudoku-by-L2G-20050714.svg.png)

A sudoku puzzle...

![37_250px-Sudoku-by-L2G-20050714_solution.svg.png](img/37_250px-Sudoku-by-L2G-20050714_solution.svg.png)

...and its solution numbers marked in red.

**Note:**

* The given board contain only digits `1-9` and the character `'.'`.
* You may assume that the given Sudoku puzzle will have a single unique solution.
* The given board size is always `9x9`.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 420 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # get a list of (row, col) of empty cells
        def get_vacant_positions(board):
            res = []
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        res.append((i, j))
            return res
        
        # get valid candidates that can be filled at (row, col)
        def get_candidates(board, row, col):
            res = set()
            for i in range(1, 10):
                res.add(str(i))
              
            # check row and col
            for i in range(9):
                if board[row][i] in res:
                    res.remove(board[row][i])
                if board[i][col] in res:
                    res.remove(board[i][col])
            
            # check box
            sr = (row // 3) * 3
            sc = (col // 3) * 3
            for i in range(sr, sr+3):
                for j in range(sc, sc+3):
                    if board[i][j] in res:
                        res.remove(board[i][j])
            
            return list(res)
        
        # fill using backtracking
        def solve(board, pos):
            if len(pos) == 0: # no more vacant positions to fill
                return True
            
            r, c = pos[0]
            candidates = get_candidates(board, r, c)
            
            if len(candidates) == 0: # no candidates, reject this path, backtrack
                return False
            
            for num in candidates:
                board[r][c] = num
                if solve(board, pos[1:]):
                    return True
                board[r][c] = '.'
            
            return False

        positions = get_vacant_positions(board)
        solve(board, positions)
```

**Solution 2: (Backtracking)**
```
Runtime: 40 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    bool isSafe(char num, vector<vector<char>>& board, int row, int col) {
        // check if num exist in row
        for (int j=0; j < 9; j++) {
            if (board[row][j]==num)
                return false;
        }

        // check if num exist in col
        for (int i=0; i < 9; i++) {
            if (board[i][col]==num)
                return false;
        }

        // check if num exist in subgrid
        int R= row - row % 3;
        int C= col - col % 3;

        for (int r=R; r < R+3; r++) {
            for (int c=C; c < C+3; c++) {
                if (board[r][c]==num)
                    return false;
            }
        }
        return true;
    }
    bool sudokuSolver(vector<vector<char>>& board, int row, int col) {
        if (row == 9) {
            return true;
        }

        if (col == 9) {
            return sudokuSolver(board, row + 1, 0);
        }

        if (board[row][col] != '.') {
            return sudokuSolver(board, row, col + 1);
        }

        for (char num = '1'; num <= '9'; num++) {
            if (isSafe(num, board, row, col)) {
                board[row][col] = num;
                bool sudokuCanBeSolvedFurther = sudokuSolver(board, row, col + 1);
                if (sudokuCanBeSolvedFurther) 
                    return true;
            }
        }
        board[row][col] = '.';
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        bool isSolved = sudokuSolver(board, 0, 0);
    }
};
```