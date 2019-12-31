529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. '**M**' represents an **unrevealed** mine, '**E**' represents an **unrevealed** empty square, '**B**' represents a **revealed** blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, **digit** ('1' to '8') represents how many mines are adjacent to this **revealed** square, and finally '**X**' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

* If a mine ('M') is revealed, then the game is over - change it to '**X**'.
* If an empty square ('E') with **no adjacent mines** is revealed, then change it to revealed blank ('B') and all of its adjacent **unrevealed** squares should be revealed recursively.
* If an empty square ('E') with **at least one adjacent mine** is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

**Example 1:**
```
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:
```
![529_minesweeper_example_1.png](img/529_minesweeper_example_1.png)

**Example 2:**
```
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:
```
![529_minesweeper_example_2.png](img/529_minesweeper_example_2.png) 

**Note:**

* The range of the input matrix's height and width is [1,50].
* The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
* The input board won't be a stage when game is over (some mines have been revealed).
* For simplicity, not mentioned rules should be ignored in this problem. For example, you **don't** need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 196 ms
Memory Usage: 18.4 MB
```
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        visited = set()

        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1),
                          (r+1, c+1),(r-1, c-1),(r-1, c+1),(r+1, c-1)
                         )
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def traverse(r, c):
            if (r, c) in visited:
                return 
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                count = 0
                for nr, nc in neighbours(r, c):
                    if board[nr][nc] in 'MX':
                        count += 1
                board[r][c] = 'B' if count == 0 else str(count)
            visited.add((r, c))
            if board[r][c] == 'B':
                for nr,nc in neighbours(r, c):
                    traverse(nr, nc)

        traverse(*click)
        return board
```

**Solution 2:(BFS)**
```
Runtime: 192 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        visited = set()

        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1),
                          (r+1, c+1),(r-1, c-1),(r-1, c+1),(r+1, c-1)
                         )
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        queue = collections.deque([click])
        while queue:
            (r, c) = queue.popleft()
            if (r, c) in visited:
                continue
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                count = 0
                for nr, nc in neighbours(r, c):
                    if board[nr][nc] in 'MX':
                        count += 1
                board[r][c] = 'B' if count == 0 else str(count)
            visited.add((r, c))
            if board[r][c] == 'B':
                for nr, nc in neighbours(r, c):
                    queue.append([nr, nc])

        return board
```