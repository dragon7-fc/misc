120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

**Note:**

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# Submissions
---

**Solution 1: (Top-Down)**
```
Runtime: 68 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)
        
        if R == 0:
            return 0
        if R == 1:
            return triangle[0][0]
        
        dp = [[triangle[0][0]]]
        for i in range(1,R):
            dp.append([0]*(i+1))
        
        for i in range(1, R):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
        
        for i in range(2, R):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                    
        return min(dp[R-1])
```

**Solution 2: (Bottom-Up)**
```
Runtime: 60 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)
        
        if R == 0:
            return 0
        if R == 1:
            return triangle[0][0]
        
        dp = triangle[-1][:]
        
        for i in range(R-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]
```