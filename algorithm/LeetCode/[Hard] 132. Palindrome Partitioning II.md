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
Runtime: 2352 ms
Memory Usage: 18.9 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dp(cur):
            if cur == cur[::-1]: return 0
            for i in range(1, len(cur)):
                if cur[:i] == cur[:i][::-1] and cur[i:] == cur[i:][::-1]:
                    return 1
            rst = len(s) - 1
            for i in range(1, len(cur)):
                if cur[:i] == cur[:i][::-1]:
                    rst = min(dp(cur[i:]), rst)
            return rst + 1

        return dp(s)
```

        return dfs(0, len(s))
```
**Solution 1: (DP Top-Down)**
```
Runtime: 2440 ms
Memory Usage: 16.9 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dp(i, j):
            if s[i:j] == s[i:j][::-1]: return 0
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1] and s[k:j] == s[k:j][::-1]:
                    return 1
            rst = float('inf')
            for k in range(i + 1, j):
                if s[i:k] == s[i:k][::-1]:
                    rst = min(rst, dp(k, j) + 1)
            return rst

        return dp(0, len(s))
```

**Solution 3: (DP Top-Down)**
```
Runtime: 1544 ms
Memory Usage: 487.2 MB
```
```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = math.inf
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j+1) + 1)
            return ans
        
        return dp(0) - 1
```
