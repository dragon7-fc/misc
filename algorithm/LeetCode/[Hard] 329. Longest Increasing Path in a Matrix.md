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
**Solution 1: (DP Top-Down)**
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

**Solution 2: (DP Top-Down)**
```
Runtime: 54 ms
Memory Usage: 16.1 MB
```
```c++
class Solution {
    bool checkLimits(int i, int j, int n, int m){
        
        return (i>=0 and i<n and j>=0 and j<m);
        
        
    }
    
    int func(vector<vector<int>> &matrix, vector<vector<int>> &dp, int i, int j, int n, int m){
        
        if(!checkLimits(i, j, n, m)) return 0;
        
        if(dp[i][j]!=-1) return dp[i][j];
        
        int c1 = 0, c2 = 0, c3 = 0, c4 =0;
        
        if(checkLimits(i+1, j, n, m) and matrix[i+1][j]>matrix[i][j]){
            c1 = func(matrix, dp, i+1, j, n, m);
        }
        
        if(checkLimits(i-1, j, n, m) and matrix[i-1][j]>matrix[i][j]){
            c2 = func(matrix, dp, i-1, j, n, m);
        }
        
        if(checkLimits(i, j+1, n, m) and matrix[i][j+1]>matrix[i][j]){
            c3 = func(matrix, dp, i, j+1, n, m);
        }
        
        if(checkLimits(i, j-1, n, m) and matrix[i][j-1]>matrix[i][j]){
            c4 = func(matrix, dp, i, j-1, n, m);
        }
        
        dp[i][j] = 1 + max(c1, max(c2, max(c3, c4)));
        
        return dp[i][j];        
        
    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        int ans = 1;
        vector<vector<int>> dp(n, vector<int> (m, -1));
        
        for(int i = 0; i<n;i++){
            for(int j=0;j<m;j++){
                if(dp[i][j]==-1){
                    ans = max(ans, func(matrix, dp, i, j, n, m));
                }
            }
        }
        return ans;
    }
};
```
