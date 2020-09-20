1594. Maximum Non Negative Product in a Matrix

You are given a `rows x cols` matrix `grid`. Initially, you are located at the top-left corner `(0, 0)`, and in each step, you can only **move right or down** in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner `(rows - 1, cols - 1)`, find the path with the **maximum non-negative product**. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative return -1.

**Notice that the modulo is performed after getting the maximum product**.

 

**Example 1:**
```
Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
```

**Example 2:**
```
Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
```

**Example 3:**
```
Input: grid = [[1, 3],
               [0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
```

**Example 4:**
```
Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
```

**Constraints:**

* `1 <= rows, cols <= 15`
* `-4 <= grid[i][j] <= 4`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 52 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(i, j): 
            """Return maximum & minimum products ending at (i, j)."""
            if i == 0 and j == 0: return grid[0][0], grid[0][0]
            if i < 0 or j < 0: return -inf, inf
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = dp(i-1, j) # from top
            mx2, mn2 = dp(i, j-1) # from left 
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = dp(m-1, n-1)
        return -1 if mx < 0 else mx % 1_000_000_007
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 48 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        Max = [[0] * n for _ in range(m)]
        Min = [[0] * n for _ in range(m)]
        Max[0][0] = grid[0][0]
        Min[0][0] = grid[0][0]
        for j in range(1, n):
            Max[0][j] = Max[0][j - 1] * grid[0][j]
            Min[0][j] = Min[0][j - 1] * grid[0][j]

        for i in range(1, m):
            Max[i][0] = Max[i - 1][0] * grid[i][0]
            Min[i][0] = Min[i - 1][0] * grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    Max[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
                    Min[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                else:
                    Max[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                    Min[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
        return Max[-1][-1] % int(1e9 + 7) if Max[-1][-1] >= 0 else -1
```