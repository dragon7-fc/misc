72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
1. Delete a character
1. Replace a character

**Example 1:**
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 68 ms
Memory Usage: 15.7 MB
```
```python
import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == -1: return j+1
            if j == -1: return i+1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)           # Nothing to do 
            else:
                return min( dfs(i, j-1)+1,     # Word1[i] Insert
                            dfs(i-1, j)+1,     # Word1[i] Delete
                            dfs(i-1, j-1)+1 )  # Word1[i] Replace 

        return dfs(len(word1)-1, len(word2)-1)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 184 ms
Memory Usage: 16.5 MB
```
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0]*(N + 1) for _ in range(M+1)]
        for i in range(1, M+1):
            dp[i][0] = i
        for j in range(1, N+1):
            dp[0][j] = j
        for i in range(1, M+1):
            for j in range(1, N+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i][j - 1],
                                    dp[i - 1][j],
                                    dp[i - 1][j - 1] ) + 1
        return dp[M][N]
```

**Solution 1: (DP Top-Down)**
```
Runtime: 92 ms
Memory Usage: 15.6 MB
```
```python
import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i == M: return N - j
            if j == N: return M - i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)           # Nothing to do 
            else:
                return min( dp(i+1, j)+1,     # Word1[i] Insert
                            dp(i, j+1)+1,     # Word1[i] Delete
                            dp(i+1, j+1)+1 )  # Word1[i] Replace 

        return dp(0, 0)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 172 ms
Memory Usage: 16.4 MB
```
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0]*(N + 1) for _ in range(M+1)]
        for i in range(M):
            dp[i][N] = M - i
        for j in range(N):
            dp[M][j] = N - j
        for i in range(M - 1, -1 , -1):
            for j in range(N - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min( dp[i][j + 1],
                                    dp[i + 1][j],
                                    dp[i + 1][j + 1] ) + 1
        return dp[0][0]
```