343. Integer Break

Given a positive integer n, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

**Example 1:**
```
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**
```
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Note:** 

* You may assume that n is not less than 2 and not larger than 58.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        dp = [0] * (n+1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            dp[i] = max(dp[j] * dp[i-j]  for j in range(2, int(i/2) + 1))
        return dp[-1]
```

**Solution 2; (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        
        @functools.lru_cache(None)
        def dfs(i):
            if i <= 1:
                return 0
            elif 2 <= i <= 3: 
                return i
            return max(j * dfs(i-j) for j in range(2, i//2 + 1))
            
        return dfs(n)
```