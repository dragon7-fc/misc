87. Scramble String

Given a string `s1`, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = ``"great"`:

```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node `"gr"` and swap its two children, it produces a scrambled string `"rgeat"`.

```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```

We say that `"rgeat"` is a scrambled string of `"great"`.

Similarly, if we continue to swap the children of nodes `"eat"` and `"at"`, it produces a scrambled string `"rgtae"`.

```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```

We say that `"rgtae"` is a scrambled string of `"great"`.

Given two strings `s1` and `s2` of the same length, determine if `s2` is a scrambled string of `s1`.

**Example 1:**
```
Input: s1 = "great", s2 = "rgeat"
Output: true
```

**Example 2:**
```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```

# Submissions
---
**Solution 1: (DFS)**

Basically we try to simulate the construction of the binary tree, and recursively split both `s1` and `s2` into same size every time and check every pair of possible splits until all splits has only one character.  
The sorted is to avoid unnecessary recursions (that grow exponentially), and it turns out to be better than set and collections.Counter in terms of runtime.

```
Runtime: 36 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def dfs(l1, r1, l2, r2):
            if r1 - l1 == 1:
                return s1[l1] == s2[l2]
            if sorted(s1[l1:r1]) != sorted(s2[l2:r2]):
                return False
            for i in range(1, r1 - l1):
                if dfs(l1, l1 + i, l2, l2 + i) and dfs(l1 + i, r1, l2 + i, r2) or \
                   dfs(l1, l1 + i, r2 - i, r2) and dfs(l1 + i, r1, l2, r2 - i):
                    return True
                
        return dfs(0, len(s1), 0, len(s2))
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 320 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        dp = [[[False for _ in s2] for _ in s2] for _ in s1]
        # dp(i, j, k) = is s1[i:i+k+1] a scramble of s2[j:j+k+1]
        n = len(s1)
        for k in range(n):
            for i in range(n-k):
                for j in range(n-k):
                    if k == 0:
                        dp[i][j][k] = s1[i] == s2[j]
                        continue
                    for v in range(k):
                        if (dp[i][j][v] and dp[i+v+1][j+v+1][k-v-1]) or (dp[i][j+k-v][v] and dp[i+v+1][j][k-v-1]):
                            dp[i][j][k] = True
                            break
        return dp[0][0][-1]

```