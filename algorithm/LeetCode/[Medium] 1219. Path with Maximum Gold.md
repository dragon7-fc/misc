1219. Path with Maximum Gold

In a gold mine `grid` of size `m * n`, each cell in this mine has an integer representing the amount of gold in that cell, `0` if it is empty.

Return the maximum amount of gold you can collect under the conditions:

* Every time you are located in a cell you will collect all the gold in that cell.
* From your position you can walk one step to the left, right, up or down.
* You can't visit the same cell more than once.
* Never visit a cell with `0` gold.
* You can start and stop collecting gold from any position in the grid that has some gold.

# Solution
---
**Solution 1: (Backtracking)**
```
Runtime: 1260 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            if not (0 <= r < R and 0 <= c < C and grid[r][c] > 0 and visited[r][c] == 0):
                return 0
            visited[r][c] = True      
            res =  grid[r][c] + max(dfs(grid, r+1, c), dfs(grid, r-1, c), dfs(grid, r, c+1), dfs(grid, r, c-1))
            visited[r][c] = False
            return res
        
        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        ans = 0
        for r in range(R):
            for c in range(C):
                ans = max(ans, dfs(grid, r, c))
        return ans
```
