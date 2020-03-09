64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example:**
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

# Submissions
---
**Solution 1: (DP, Bottom-Up)**
```
Runtime: 60 ms
Memory Usage: N/A
```
```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        mps = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    mps[i][j] = grid[i][j]
                elif i == 0:
                    mps[i][j] = mps[i][j-1] + grid[i][j]
                elif j == 0:
                    mps[i][j] = mps[i-1][j] + grid[i][j]
                else:
                    mps[i][j] = min(mps[i-1][j], mps[i][j-1]) + grid[i][j]
        return mps[-1][-1]
```

**Solution 2: (DP Top-Down, DFS, Post-Order)**
```
Runtime: 112 ms
Memory Usage: 18.6 MB
```
```python
import functools
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 8 and n == 0:
            return 0
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            if i >= m or j >= n:
                return float('inf')
            return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)
    
```