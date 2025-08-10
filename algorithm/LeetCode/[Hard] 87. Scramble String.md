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

**Solution 3: (DP Top-Down)**
```
Runtime: 66 ms
Memory: 7.9 MB
```
```c++
class Solution {
public:
    bool isScramble(string s1, string s2) {
        int n = (int) s1.size();
        bool vis[n][n][n][n];
        bool dp[n][n][n][n];
        memset(vis, false, sizeof(vis));
        memset(dp, false, sizeof(dp));

        // we are always calling the function such that, the substring we are checking on both the
        // substrings are of same length, i.e. (r1 - l1 + 1 == r2 - l2 + 1)

        // helper takes in two substrings of both string
        // and returns whether they are scamble of each other
        function<bool(int, int, int, int)> helper = [&] (int l1, int r1, int l2, int r2) {
            if (vis[l1][r1][l2][r2]) {
                return dp[l1][r1][l2][r2];
            }
            vis[l1][r1][l2][r2] = true;
            bool isSame = true;
            for (int i = l1, j = l2; i <= r1 && j <= r2; i++, j++) {
                if (s1[i] != s2[j]) {
                    isSame = false;
                    break;
                }
            }
            
            // is already same, simply return true
            if (isSame) {
                dp[l1][r1][l2][r2] = true;
                return true;
            }

            bool res = false;
            for (int i = l1; i < r1; i++) {
                // opt1: prefix1 matches to prefix2 and suffix1 matches to suffix2
                res |= (helper(l1, i, l2, l2 + (i - l1)) && helper(i + 1, r1, l2 + (i - l1) + 1, r2));

                // opt2: prefix1 matches to suffix2 and prefix2 matches to suffix1
                res |= (helper(l1, i, r2 - (i - l1), r2) && helper(i + 1, r1, l2, r2 - (i - l1) - 1));
            }
            dp[l1][r1][l2][r2] = res;
            return res;
        };

        return helper(0, n - 1, 0, n - 1);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 56 ms
Memory: 10.4 MB
```
```c++
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1 == s2) {
            return true;
        }
        string s1_cpy = s1, s2_cpy = s2;
        sort(s1_cpy.begin(), s1_cpy.end());
        sort(s2_cpy.begin(), s2_cpy.end());
        if (s1_cpy != s2_cpy) {
            return false;
        }
        int n = s1.size();
        vector<vector<vector<bool>>> dp(n, vector<vector<bool>>(n, vector<bool>(n+1)));
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                dp[i][j][1] = (s1[i] == s2[j]);
            }
        }
        for (int length = 2; length < n+1; length ++) {
            for (int i = 0; i < n-length+1; i ++) {
                for (int j = 0; j < n-length+1; j ++) {
                    for (int k = 1; k < length; k ++) {
                        if ((dp[i][j][k] && dp[i+k][j+k][length-k]) || (dp[i][j+length-k][k] && dp[i+k][j][length-k])) {
                            dp[i][j][length] = true;
                            break;
                        }
                    }
                }
            }
        }
        
        return dp[0][0][n];
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 12 ms, Beats 28.30%
Memory: 19.76 MB, Beats 12.30%
```
```c++
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size(), i, k;
        vector<vector<int>> dp(n, vector<int>(n));
        for (i = 0; i < n; i ++) {
            dp[i][i] = -piles[i];
        }
        for (k = 2; k <= n; k ++) {
            for (i = 0; i <= n-k; i ++) {
                if (k%2 == 0) {
                    dp[i][i+k-1] = max(piles[i] + dp[i+1][i+k-1], piles[i+k-1] + dp[i][i+k-2]);
                } else {
                    dp[i][i+k-1] = max(-piles[i] + dp[i+1][i+k-1], -piles[i+k-1] + dp[i][i+k-2]);
                }
            }
        }
        return dp[0][n-1] > 0;
    }
};
````
