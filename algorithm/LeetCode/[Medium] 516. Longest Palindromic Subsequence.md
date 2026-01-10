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

**Solution 4: (DP Top-Down)**
```
Runtime: 87 ms
Memory: 73 MB
```
```c++
class Solution {
    int dfs(int i, int j, string &s, vector<vector<int>> &dp) {
        if (i == j) {
            dp[i][i] = 1;
        } else if (i+1 == j) {
            if (s[i] == s[j]) {
                dp[i][j] = 2;
            } else {
                dp[i][j] = 1;
            }
        }
        if (dp[i][j]) {
            return dp[i][j];
        }
        int rst;
        if (s[i] == s[j]) {
            rst = 2 + dfs(i+1, j-1, s, dp);
        } else {
            rst = max(dfs(i+1, j, s, dp), dfs(i, j-1, s, dp));
        }
        dp[i][j] = rst;
        return rst;
    }
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size(), ans = 1;
        vector<vector<int>> dp(n, vector<int>(n));
        return dfs(0, n-1, s, dp);
    }
};
```

**Solution 5: (DP Bottom-Up)**

    s = "b b b a b"
dp       0 1 2 3 4  j
b 0      1 2 3 3 4 <
b 1        1 2 2 3
b 2          1 1 3
a 3            1 1
b 4              1
i
```
Runtime: 144 ms
Memory: 73 MB
```
```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size(), ans = 1;
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 0; i < n; i ++) {
            dp[i][i] = 1;
        }
        for (int i = n-2; i >= 0; i --) {
            for (int j = i+1; j < n; j ++) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i+1][j-1];
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]);
                }
            }
        }
        return dp[0][n-1];
    }
};
```

**Solution 6: (DP Bottom-Up 1-D)**
```
Runtime: 98 ms
Memory: 72.3 MB
```
```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        vector<int> dp(n, 0);
        for (int i = n - 1; i >= 0; i--) {
            vector<int> newdp(n, 0);
            newdp[i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    newdp[j] = 2 + dp[j-1];
                } else {
                    newdp[j] = max(dp[j], newdp[j-1]);
                }
            }
            dp = newdp;
        }
        return dp[n-1];
    }
};
```

**Solution 7: (DP Bottom-Up)**

   b b b a b
b  1 2 3 3 2
b    1 2 2 3
b      1 1 3
a        1 1
b          1

```
Runtime: 81 ms, Beats 53.13%
Memory: 75.88 MB, Beats 63.10%
```
```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size(), i, k, ans = 1;
        vector<vector<int>> dp(n, vector<int>(n, 1));
        for (i = 0; i < n; i ++) {
            dp[i][i] = 1;
            if (i+1 < n && s[i] == s[i+1]) {
                dp[i][i+1] = 2;
                ans = 2;
            }
        }
        for (k = 3; k <= n; k ++) {
            for (i = 0; i+k <= n; i ++) {
                dp[i][i+k-1] = max(dp[i][i+k-2], dp[i+1][i+k-1]);
                if (s[i] == s[i+k-1]) {
                    dp[i][i+k-1] = max(dp[i][i+k-1], dp[i+1][i+k-2] + 2);
                    ans = max(ans, dp[i][i+k-1]);
                }
            }
        }
        return ans;
    }
};
```
