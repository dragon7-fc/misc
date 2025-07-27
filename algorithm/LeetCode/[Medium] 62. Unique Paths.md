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
**Solution 1: (DP Bottom-Up)**
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

**Solution 2: (DP Top-Down, DFS)**
```
Runtime: 28 ms
Memory Usage: 13.4 MB
```
```python
import functools
class Solution:
    @functools.lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
```

**Solution 3: (DP Top-Down, DFS, Post-Order)**
```
Runtime: 24 ms
Memory Usage: 13 MB
```
```python
import functools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache
        def dfs(i, j):
            if i == m-1 or j == n-1:
                return 1
            count = 0
            if i < m-1:
                count += dfs(i+1, j)    # go down
            if j < n-1:
                count += dfs(i, j+1)    # go right
            return count
        return dfs(0, 0)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        int dp[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dp[i][j] = (i==0 && j==0) ? 1 : 0;
                if(i > 0)
                     dp[i][j] +=  dp[i-1][j];
                if(j > 0)
                     dp[i][j] +=  dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```

**Solution 5: (DP Bottom-Up 1-D)**

       0   1   2   3   4   5   6
    0  1   1   1   1   1   1   1
    1  1   2   3   4   5   6   7
    2  1   3   6  10  15  21  28

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.14 MB, Beats 84.51%
```
```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        int i, j;
        vector<int> dp(n, 1);
        for (i = 1; i < m; i ++) {
            for (j = 1; j < n; j ++) {
                dp[j] += dp[j-1];
            }
        }
        return dp[n-1];
    }
};
```
