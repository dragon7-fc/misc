712. Minimum ASCII Delete Sum for Two Strings

Given two strings `s1, s2`, find the lowest ASCII sum of deleted characters to make two strings equal.

**Example 1:**

```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

**Example 2:**

```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```

**Note:**

* `0 < s1.length`, `s2.length <= 1000`.
* All elements of each string will have an ASCII value in `[97, 122]`.

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition and Algorithm**

Let `dp[i][j]` be the answer to the problem for the strings `s1[i:], s2[j:]`.

When one of the input strings is empty, the answer is the ASCII-sum of the other string. We can calculate this cumulatively using code like `dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i)`.

When `s1[i] == s2[j]`, we have `dp[i][j] = dp[i+1][j+1]` as we can ignore these two characters.

When `s1[i] != s2[j]`, we will have to delete at least one of them. We'll have `dp[i][j]` as the minimum of the answers after both deletion options.

The solutions presented will use bottom-up dynamic programming.

```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]
```

**Complexity Analysis**

* Time Complexity: $O(M*N)$, where $M, N$ are the lengths of the given strings. We use nested for loops: each loop is $O(M)$ and $O(N)$ respectively.

* Space Complexity: $O(M*N)$, the space used by `dp`.

# Submissions
---
**Solution 1: (Dynamic Programming, Bottom-Up)**

```
Runtime: 712 ms
Memory Usage: 18.2 MB
```
```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 1132 ms
Memory Usage: 211.2 MB
```
```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        M, N = len(s1), len(s2)
        
        @lru_cache(None)
        def dfs(i, j): 
            """Return sum of deleted chars for s1[:i] and s2[:j] to make them equal"""
            if i == M: return sum(map(ord, s2[j:]))
            if j == N: return sum(map(ord, s1[i:]))
            if s1[i] == s2[j]: return dfs(i+1, j+1)
            else: return min(dfs(i+1, j) + ord(s1[i]), dfs(i, j+1) + ord(s2[j]))
            
        return dfs(0, 0)
```