329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

**Example 1:**
```
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**
```
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

# Submissions
---
**Solution 1: (DP, DFS)**
```
Runtime: 364 ms
Memory Usage: 17.3 MB
```
```python
import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        R, C = len(matrix), len(matrix[0])
        
        @functools.lru_cache(None)
        def dfs(r, c):
            val = matrix[r][c]
            return 1 + max(dfs(r-1, c) if r and val < matrix[r-1][c] else 0,
                            dfs(r+1, c) if r < R-1 and val < matrix[r+1][c] else 0,
                            dfs(r, c-1) if c and val < matrix[r][c-1] else 0,
                            dfs(r, c+1) if c < C-1 and val < matrix[r][c+1] else 0)
        
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(dfs(r, c), res)
        
        return res
```