62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![robot_maze](img/62_robot_maze.png)

Above is a 7 x 3 grid. How many possible unique paths are there?

**Note:** m and n will be at most 100.

**Example 1:**
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

**Example 1:**
```
Input: m = 7, n = 3
Output: 28
```

# Submissions
---
**Solution:**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            ans[0][i] = 1
        for i in range(n):
            ans[i][0] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
                
        return ans[n-1][m-1]    
```