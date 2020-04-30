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
**Solution 1: (DP)**

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