279. Perfect Squares

Given a positive integer `n`, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to `n`.

**Example 1:**
```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

# Submissions
---
**Solution 1:**
```
Runtime: 2268 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = min([dp[i-j*j] for j in range(1,int(i**.5)+1)])+1
        return dp[n]
```