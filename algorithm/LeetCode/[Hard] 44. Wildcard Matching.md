44. Wildcard Matching

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`.
```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
```
The matching should cover the entire input string (not partial).

**Note:**

* `s` could be empty and contains only lowercase letters `a-z`.
* `p` could be empty and contains only lowercase letters `a-z`, and characters like `?` or `*`.

**Example 1:**
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**
```
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**
```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

**Example 4:**
```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```

**Example 5:**
```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 604 ms
Memory Usage: 123.5 MB
```
```python
import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        
        @functools.lru_cache(None)
        def dfs(i, j) :
            if i > M or j > N : return False 
            elif i == M:
                if j == N : return True
                elif p[j] == '*':
                    return dfs(i, j+1)
                else:
                    return False
            elif j == N:
                return False
            if s[i] == p[j] or p[j]== '?':
                return dfs(i + 1, j + 1)
            elif p[j] == '*':
                return dfs(i, j + 1) or dfs(i + 1, j) or dfs(i + 1, j + 1)
            else:
                return False
            
        return dfs(0, 0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 812 ms
Memory Usage: 21.1 MB
```
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)    
        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[-1][-1] = True
        for j in range(N - 1, -1, -1):
            if p[j] == '*':
                dp[M][j] = True
            else:
                break
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j + 1]

        return dp[0][0]
```

**Solution 3: (DP Bottom-Up)**

      a a
    a   v
          v
      a a
    * v v
          v
      c b
    ?  
    a
          v
                vi    
      a d c e b 
    * v
    a v
    * v v v v v
  j>b         v
                v
                
      ""
    * v
    * v
    * v
    * v
    * v
    * v
      v  

```
Runtime: 39 ms, Beats 24.50%
Memory: 31.67 MB, Beats 22.13%
```
```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size(), i, j;
        vector<vector<int>> dp(m+1, vector<int>(n+1));
        dp[m][n] = 1;
        for (j = n-1; j >= 0; j --) {
            for (i = m; i >= 0; i --) {
                if (i < m && (s[i] == p[j] || p[j] == '?')) {
                    dp[i][j] = dp[i+1][j+1];
                } else if (p[j] == '*') {
                    dp[i][j] = dp[i][j+1];
                    if (i < m) {
                        dp[i][j] |= dp[i+1][j];
                        dp[i][j] |= dp[i+1][j+1];
                    }
                }
            }
        }
        return dp[0][0];
    }
};
```
