132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

**Example:**
```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 224 ms
Memory Usage: 13.6 MB
```
```python
import functools
class Solution:
    def minCut(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dfs(s):
            if s == s[::-1]: return 0
            for i in range(1, len(s)):
                if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                    return 1
            ans = len(s) - 1
            for i in range(1, len(s)):
                if s[:i] == s[:i][::-1]:
                    ans = min(dfs(s[i:]), ans)
            return ans + 1

        return dfs(s)
```

**Solution 2: (DP Top-Down)**
```
Runtime: 236 ms
Memory Usage: 13.6 MB
```
```python
import functools
class Solution:
    def minCut(self, s: str) -> int:   

        @functools.lru_cache(None)
        def dfs(i, j):
            if s[i:j] == s[i:j][::-1]: return 0
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1] and s[k:j] == s[k:j][::-1]:
                    return 1
            rst = float('inf')
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1]:
                    rst = min(rst, dfs(k, j) + 1)
            return rst

        return dfs(0, len(s))
```