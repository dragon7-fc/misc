115. Distinct Subsequences

Given a string **S** and a string **T**, count the number of distinct subsequences of **S** which equals **T**.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).

**Example 1:**
```
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

**Example 2:**
```
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 304 ms
Memory Usage: 92.1 MB
```
```python
import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if j == N:
                return 1
            elif i == M:
                return 0
            if s[i] == t[j]:
                return dfs(i + 1, j) + dfs(i + 1, j + 1)
            else:
                return dfs(i + 1, j)
            
        return dfs(0, 0)
```

**Solution 2: (DP Top-Down)**
```
Runtime: 144 ms
Memory Usage: 48.1 MB
```
```python
import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        @functools.lru_cache(None)
        def dfs(i, j):
            if j == 0:
                return 1
            elif i == 0:
                return 0
            if s[i-1] == t[j-1]:
                return dfs(i - 1, j) + dfs(i - 1, j - 1)
            else:
                return dfs(i - 1, j)
            
        return dfs(M, N)
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 148 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [[0]*(N + 1) for _ in range(M + 1)]  #dp[m+1][n+1] means s[:m+2] t[:n+2]
        for i in range(M+1):
            dp[i][0] = 1
        for i in range(1,M+1):
            for j in range(1,N+1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]  # drop s[i]
                    
        return dp[-1][-1]
```

**Solution 4: (DP Bottom-Up)**

    r  a  b  b  b  i  t
f   3
a      3
b         3  1  
b         3  2  1
i                  1
t                     1
    1  1  1  1  1  1  1  1

    b  a  b  g  b  a  g 
b   5     2     1
a      3           1
g            2        1
    1  1  1  1  1  1  1  1


```
Runtime: 29 ms, Beats 61.46%
Memory: 44.09 MB, Beats 40.82%
```
```c++
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size(), i, j;
        vector<int> pre(m+1, 1), cur(m+1);
        for (j = n-1; j >= 0; j --) {
            for (i = m-1; i >= 0; i --) {
                cur[i] += cur[i+1];
                if (s[i] == t[j]) {
                    cur[i] += (long long)pre[i+1];
                }
            }
            pre = move(cur);
            cur.resize(m+1);
        }
        return pre[0];
    }
};
```
        
**Solution 5: (DP Bottom-Up)**

     b  a  g
   1
b  1 1 
a  1 1  1
b  1 2  1
g  1 2  1  1 
b    3  1  1
a       4  1
g          5

```
Runtime: 15 ms, Beats 84.30%
Memory: 26.20 MB, Beats 76.89%
```
```c++
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size(), i, j;
        vector<int> pre(n+1), cur(n+1);
        pre[0] = 1;
        for (i = 0; i < m; i ++) {
            cur[0] = 1;
            for (j = 0; j < n; j ++) {
                if (s[i] == t[j]) {
                    cur[j+1] = (long long)pre[j] + pre[j+1];
                } else {
                    cur[j+1] = pre[j+1];
                }
            }
            pre = move(cur);
            cur.resize(n+1);
        }
        return pre[n];
    }
};
```
