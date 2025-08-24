1277. Count Square Submatrices with All Ones

Given a m * n `matrix` of ones and zeros, return how many **square** submatrices have all ones.

 

**Example 1:**
```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

**Example 2:**
```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
``` 

**Constraints:**

* `1 <= arr.length <= 300`
* `1 <= arr[0].length <= 300`
* `0 <= arr[i][j] <= 1`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

1. get all possible squares for each position, dp[i][j] = min(dp[i-1][j], dp[i][j-1] ,dp[i-1][j-1]) + 1
1. add all possible squares together

```
Runtime: 636 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if  matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1] ,matrix[i-1][j-1]) + 1
        return sum([ sum(x) for x in matrix])  
```

**Solution 2: (DP Top-Down)**
```
Runtime: 920 ms
Memory Usage: 58.3 MB
```
```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        ans = 0
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0 or j == 0:
                return matrix[i][j]
            up = dp(i, j-1)
            left = dp(i-1, j)
            upleft = dp(i-1, j-1)
            if matrix[i][j] == 1:
                return 1 + min(up, left, upleft)
            else:
                return 0
        
        for r in range(R):
            for c in range(C):
                ans += dp(r, c)
        return ans
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 13 ms
Memory: 28.94 MB
```
```c++
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), ans = 0;
        vector<vector<int>> dp(m, vector<int>(n));
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                dp[i][j] = matrix[i][j];
                if (i&&j && dp[i][j]) {
                    dp[i][j] += min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
                }
                ans += dp[i][j];
            }
        }
        return ans;
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 3 ms, Beats 82.96%
Memory: 30.14 MB, Beats 82.73%
```
```c++
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), i, j, ans;
        vector<int> pre = matrix[0], cur;
        ans = accumulate(pre.begin(), pre.end(), 0);
        for (i = 1; i < m; i ++) {
            cur.resize(n);
            cur[0] = matrix[i][0];
            ans += cur[0];
            for (j = 1; j < n; j ++) {
                if (matrix[i][j]) {
                    cur[j] = min({cur[j-1], pre[j], pre[j-1]}) + 1;
                }
                ans += cur[j];
            }
            pre = move(cur);
        }
        return ans;
    }
};
```
