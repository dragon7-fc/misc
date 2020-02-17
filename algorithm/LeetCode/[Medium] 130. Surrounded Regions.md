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
Runtime: 148 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R, C = len(board), len(board[0])
        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        def dfs(r, c):
            board[r][c] = "*"
            for nr, nc in neighbours(r, c):
                if board[nr][nc] == 'O':
                    dfs(nr, nc)
                    
        # Cells at the border cannot be captured, mark all of them to be
        # not captured
        for c in range(C):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[R - 1][c] == 'O':
                dfs(R - 1, c)
        for r in range(R):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][C - 1] == 'O':
                dfs(r, C - 1)
                
        # Mark any remaining "O" to be captured
        # Revert any uncaptureable "*" back to "O"
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "*":
                    board[r][c] = "O"
```

**Solution 2: (BFS)**
```
Runtime: 144 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R, C = len(board), len(board[0])
        q = collections.deque()
        for c in range(C):
            q.append((0, c))
            q.append((R - 1, c))
        for r in range(R):
            q.append((r, 0))
            q.append((r, C - 1))
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

**Solution 3: (Union Find)**
```
Runtime: 448 ms
Memory Usage: 14.7 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return              
        R, C = len(board), len(board[0])
        dummy = R*C
        dsu = DSU(R*C + 1)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    if r == 0 or r == R-1 or c == 0 or c == C-1:
                        dsu.union(r*C + c, dummy)
                    else:
                        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if board[nr][nc] == 'O':
                                dsu.union(r*C + c, nr*C + nc)              
        for r in range(R):
            for c in range(C):
                if dsu.find(dummy) == dsu.find(r*C + c):
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'        
```