130. Surrounded Regions

Given a 2D `board` containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:**
```
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
```

**Solution 1: (DFS)**
```
Runtime: 144 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        R = len(board)
        C = len(board[0])
        def dfs(i, j):
            if i < 0 or i >= R or j < 0 or j >= C or board[i][j] == "*":
                return

            if board[i][j] == "X":
                return

            board[i][j] = "*"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        # Cells at the border cannot be captured, mark all of them to be
        # not captured
        
        for j in range(C):
            dfs(0, j)
            dfs(R - 1, j)
        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)
        
        # Mark any remaining "O" to be captured
        # Revert any uncaptureable "*" back to "O"
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"
```

**Solution 2: (BFS)**
```
Runtime: 140 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R = len(board)
        C = len(board[0])
        q = collections.deque()
        for j in range(C):
            q.append((0, j))
            q.append((R - 1, j))
        for i in range(R):
            q.append((i, 0))
            q.append((i, C - 1))
        while q:
            r, c = q.popleft()
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                # modify the value from O to N
                board[r][c] = "*"
                # append the surrouding cells to queue.
                q.append((r, c+1))
                q.append((r, c-1))
                q.append((r-1, c))
                q.append((r+1, c))  
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"
```