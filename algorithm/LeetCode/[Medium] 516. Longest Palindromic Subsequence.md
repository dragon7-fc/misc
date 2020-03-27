516. Longest Palindromic Subsequence

Given a string `s`, find the longest palindromic subsequence's length in `s`. You may assume that the maximum length of `s` is 1000.

**Example 1:**
```
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
```

**Example 2:**
```
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
```

## Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 1340 ms
Memory Usage: 30.4 MB
```
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0]*(N) for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = 1

                    
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):                    
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    
        return dp[0][-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 836 ms
Memory Usage: 226 MB
```
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 1
            elif i > j: return 0
            if s[i] == s[j]:
                return 2 + dp(i+1, j-1)
            else:
                return max(dp(i+1, j), dp(i, j-1))
            
        return dp(0, N-1)
```