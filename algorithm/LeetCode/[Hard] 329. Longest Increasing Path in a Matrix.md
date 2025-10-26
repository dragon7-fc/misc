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

**Solution 2: (DP Bottom-Up)**
```
Runtime: 67 ms
Memory: 16 MB
```
```c++
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = size(matrix), n = size(matrix[0]), ans = 0;
        vector<int> idx(m*n);
        iota(begin(idx), end(idx), 0);
        sort(begin(idx), end(idx), [&](auto& a, auto& b){return matrix[a/n][a%n]<matrix[b/n][b%n];});
        int dp[m][n];
        int dx[4]{0, 0, -1, 1};
        int dy[4]{1, -1, 0, 0};
        memset(dp, 0, sizeof(dp));
        for (int i : idx){
            int x = i/n, y = i%n;
            for (int k = 0; k < 4; ++k){
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (nx >= 0 && ny >= 0 && nx < m && ny < n && matrix[x][y] > matrix[nx][ny]){
                    dp[x][y] = max(dp[x][y], dp[nx][ny]);
                }
            }
            ans = max(++dp[x][y], ans);
        }
        return ans;
    }
};
```

**Solution 3: (DP Top-Down)**
```
Runtime: 8 ms, Beats 77.87%
Memory: 20.91 MB, Beats 54.82%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
    int dfs(int r, int c, vector<vector<int>> &dp, vector<vector<int>> &matrix) {
        if (dp[r][c]) {
            return dp[r][c];
        }
        int rst = 0, nr, nc;
        for (int d = 0; d < 4; d ++) {
            nr = r + dd[d];
            nc = c + dd[d + 1];
            if (0 <= nr && nr < matrix.size() && 0 <= nc && nc < matrix[0].size() && matrix[nr][nc] > matrix[r][c]) {
                rst = max(rst, dfs(nr, nc, dp, matrix));
            }
        }
        dp[r][c] = rst + 1;
        return dp[r][c];
    }

public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n));
        int ans = 0;
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                ans = max(ans, dfs(i, j, dp, matrix));
            }
        }
        return ans;
    }
};
```
