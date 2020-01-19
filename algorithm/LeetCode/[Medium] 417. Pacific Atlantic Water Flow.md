417. Pacific Atlantic Water Flow

Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

**Note:**

* The order of returned grid coordinates does not matter.
* Both `m` and `n` are less than 150.
 

**Example:**
```
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 280 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not matrix:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)
```

**Solution 2: (BFS)**
```
Runtime: 316 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return 
        row = len(matrix)
        col = len(matrix[0])
        pacific = [[False for _ in range(col)] for _ in range(row)]
        atlantic = [[False for _ in range(col)] for _ in range(row)]
        queue_p = []
        queue_a = []
        re = []
        for i in [0,row-1]:
            for j in range(col):
                if i == 0:
                    pacific[i][j]= True
                    queue_p.append((i,j))
                if i == row-1:
                    atlantic[i][j] = True
                    queue_a.append((i,j))
        for i in range(row):
            for j in [0,col-1]:
                if j == 0:
                    pacific[i][j] = True
                    queue_p.append((i,j))
                if j == col-1:
                    atlantic[i][j] = True
                    queue_a.append((i,j))
        while queue_p:
            a, b = queue_p.pop(0)
            for m, n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                if 0 <= m < row and 0 <= n < col and not pacific[m][n] and matrix[m][n] >= matrix[a][b]:
                    pacific[m][n] = True
                    queue_p.append((m,n))
   
                
        while queue_a:
            a, b = queue_a.pop(0)
            for m, n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                if 0 <= m < row and 0 <= n < col and not atlantic[m][n] and matrix[m][n] >= matrix[a][b]:
                    atlantic[m][n]= True
                    queue_a.append((m,n))
   

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    re.append([i,j])
        return re
```