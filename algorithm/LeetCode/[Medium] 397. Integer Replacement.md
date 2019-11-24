397. Integer Replacement

Given a positive integer `n` and you can do operations as follow:

* If `n` is even, replace `n` with `n/2`.
* If `n` is odd, you can replace `n` with either `n + 1` or `n - 1`.

What is the minimum number of replacements needed for `n` to become `1`?

**Example 1:**
```
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
```

**Example 2:**
```
Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
```
# Submissions
---
**Solution 1:**
```
Runtime: 20 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        dic = {}
        def dp(n):
            if n == 1:
                return 0
            if n in dic:
                return dic[n]
            if n%2==0:
                res = 1 + dp(n>>1)
            else:
                res = 1 + min(dp(n+1),dp(n-1))
            dic[n] = res
            return res
        
        return dp(n)
```