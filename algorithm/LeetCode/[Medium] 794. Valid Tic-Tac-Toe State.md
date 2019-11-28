794. Valid Tic-Tac-Toe State

A Tic-Tac-Toe board is given as a string array `board`. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The `board` is a 3 x 3 array, and consists of characters `" "`, `"X"`, and `"O"`.  The `" "` character represents an empty square.

Here are the rules of Tic-Tac-Toe:

* Players take turns placing characters into empty squares (" ").
* The first player always places "X" characters, while the second player always places "O" characters.
* "X" and "O" characters are always placed into empty squares, never filled ones.
* The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
* The game also ends if all squares are non-empty.
* No more moves can be played if the game is over.

**Example 1:**
```
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".
```

**Example 2:**
```
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.
```

**Example 3:**
```
Input: board = ["XXX", "   ", "OOO"]
Output: false
```

**Example 4:**
```
Input: board = ["XOX", "O O", "XOX"]
Output: true
```

**Note:**

* `board` is a length-3 array of strings, where each string `board[i]` has length `3`.
* Each `board[i][j]` is a character in the set `{" ", "X", "O"}`.

# Submissions
---
**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```python
#A board is invalid in the case that: 
#   1. There are more Os than Xs, this is invalid because the X player is the one       that starts
#   2. There are 2 or more Xs than 0s, this is because a Tic Tac Toe game can only      have the same amount of Xs and Os or 1 more X than an O
#   3. Only 1 person can win, so the case that both players got 3 in a row              (diagonally, vertically or horizontally) is an invalid one
#   4. In the case that X wins, since X always goes before O, there will be exactly     1 more X than an O on the board, any other case in which X wins is an invalid       one
#   5. In the case that O wins, since 0 always goes after X, there will be the same     Xs as Os on the board, any other case in which 0 wins is an invalid one

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def diagonalCheck(board,char):
            if (board[0][0] == char and board[1][1] == char and board[2][2] == char) or (board[0][2] == char and board[1][1] == char and board[2][0] == char):
                return True
            else:
                return False
    
        def horizontalCheck(board,char):
            if (board[0][0] == char and board[0][1] == char and board[0][2] == char) or (board[1][0] == char and board[1][1] == char and board[1][2] == char) or (board[2][0] == char and board[2][1] == char and board[2][2] == char):
                return True
            else:
                return False
    
        def verticalCheck(board,char):
            if (board[0][0] == char and board[1][0] == char and board[2][0] == char) or (board[0][1] == char and board[1][1] == char and board[2][1] == char) or (board[0][2] == char and board[1][2] == char and board[2][2] == char):
                return True
            else:
                return False
        
        ocount = 0
        xcount = 0
        for row in board:
            for char in row:
                if char == "O":
                    ocount+=1
                elif char == "X":
                    xcount+=1
        #Cases 1 and 2
        if ocount > xcount or (xcount >= ocount and xcount > ocount+1):
            return False
        
        xcheck = (diagonalCheck(board,"X") or horizontalCheck(board,"X") or verticalCheck(board,"X"))
        ocheck = (diagonalCheck(board,"O") or horizontalCheck(board,"O") or verticalCheck(board,"O"))
        
        #Case 3
        if xcheck == True and ocheck == True:
            return False
        
        #Case 4
        if xcheck == True and ocheck == False and xcount != ocount +1:
            return False
        
        #Case 5
        if xcheck == False and ocheck == True and xcount != ocount:
            return False
        
        else:
            return True
```