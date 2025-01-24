3393. Count Paths With the Given XOR Value

You are given a 2D integer array `grid` with size `m x n`. You are also given an integer `k`.

Your task is to calculate the number of paths you can take from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)` satisfying the following **constraints**:

* You can either move to the right or down. Formally, from the cell `(i, j)` you may move to the cell `(i, j + 1)` or to the cell `(i + 1, j)` if the target cell exists.
* The `XOR` of all the numbers on the path must be equal to `k`.

Return the total number of such paths.

Since the answer can be very large, return the result modulo `10^9 + 7`.

 

**Example 1:**
```
Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11

Output: 3

Explanation: 

The 3 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
```

**Example 2:**
```
Input: grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2

Output: 5

Explanation:

The 5 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)
(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)
(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)
```

**Example 3:**
```
Input: grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10

Output: 0
```
 

**Constraints:**

* `1 <= m == grid.length <= 300`
* `1 <= n == grid[r].length <= 300`
* `0 <= grid[r][c] < 16`
* `0 <= k < 16`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 173 ms
Memory: 146.60 MB
```
```c++
class Solution {
public:
    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), i, j, ck, MOD=1e9+7;
        vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(n, vector<long long>(16)));
        dp[0][0][grid[0][0]] = 1;
        for (i = 1; i < m; i ++) {
            for (ck = 0; ck < 16; ck++) {
                dp[i][0][ck^grid[i][0]] += dp[i-1][0][ck];
            }
        }
        for (j = 1; j < n; j ++) {
            for (ck = 0; ck < 16; ck++) {
                dp[0][j][ck^grid[0][j]] += dp[0][j-1][ck];
            }
        }
        for (i = 1; i < m; i ++) {
            for (j = 1; j < n; j ++) {
                for (ck = 0; ck < 16; ck ++) {
                    dp[i][j][ck^grid[i][j]] += dp[i-1][j][ck];
                    dp[i][j][ck^grid[i][j]] %= MOD;
                    dp[i][j][ck^grid[i][j]] += dp[i][j-1][ck];
                    dp[i][j][ck^grid[i][j]] %= MOD;
                }
            }
        }
        return dp[m-1][n-1][k];
    }
};
```
