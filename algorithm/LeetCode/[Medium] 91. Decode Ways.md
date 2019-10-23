91. Decode Ways

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

**Example 1:**
```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**
```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        
        dp = [0] * (n + 1)
        if s[n-1] != '0':
            dp[n-1] = 1
        dp[n] = 1 # dp[n] is auxiliary
        
        for i in range(n-2, -1, -1):
            one = s[i]
            two = s[i: i+2]
            if '1' <= one <= '9':
                dp[i] = dp[i+1]
            if '10' <= two <= '26':
                dp[i] += dp[i+2]
                
        return dp[0]
```

**Solution 2:**
```
Runtime: 36 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            if s[i - 1] > '0':
                dp[i] = dp[i - 1]
                if i > 1 and s[i - 2] > '0' and (s[i - 2], s[i - 1]) <= ('2', '6'):
                    dp[i] += dp[i - 2]
            else:
                if i > 1 and s[i - 2] < '3' and s[i - 2] > '0':
                    dp[i] = dp[i - 2]
                else:
                    return 0
        return dp[-1]
```