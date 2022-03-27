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

**Solution 3: (DP Bottom-Up)**
```
Runtime: 168 ms
Memory Usage: 10.9 MB
```
```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        string t = s;
        reverse(s.begin(),s.end());
        return LCS(t,s);
    }
    
    int LCS(string X, string Y)
    {
        int i,j;
        int n = X.size();
        int m = Y.size();
        int dp[n+1][m+1];
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=m;j++)
            {
                if(i==0 || j==0)
                {
                    dp[i][j] = 0;
                }
                else if(X[i-1]==Y[j-1])
                {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else
                {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
                }
            }
        }
        return dp[n][m];
    }
};
```
