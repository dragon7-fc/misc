999. Available Captures for Rook

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:

![999_example_1_improved](img/999_example_1_improved.png)

```
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
```

**Example 2:**

![999_example_2_improved](img/999_example_2_improved.png)

```
Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.
```

**Example 3:**

![999_example_3_improved](img/999_example_3_improved.png)

```
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
```

**Note:**

1. `board.length` == `board[i].length` == 8
1. `board[i][j]` is either 'R', '.', 'B', or 'p'
1. There is exactly one cell with `board[i][j]` == 'R'

# Submissions
---
**Solution 1:**
```
untime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R = len(board)
        C = len(board[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'R':
                    e = range(c, C)
                    w = range(c, -1, -1)
                    n = range(r, -1, -1)
                    s = range(r, R)
                    for i in e:
                        if board[r][i] == 'B':
                            break
                        elif board[r][i] == 'p':
                            ans += 1
                            break
                    for i in w:
                        if board[r][i] == 'B':
                            break
                        elif board[r][i] == 'p':
                            ans += 1
                            break
                    for i in n:
                        if board[i][c] == 'B':
                            break
                        elif board[i][c] == 'p':
                            ans += 1
                            break
                    for i in s:
                        if board[i][c] == 'B':
                            break
                        elif board[i][c] == 'p':
                            ans += 1
                            break
                    return ans
```