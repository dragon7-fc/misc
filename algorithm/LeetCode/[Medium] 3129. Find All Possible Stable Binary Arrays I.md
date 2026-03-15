3129. Find All Possible Stable Binary Arrays I

You are given `3` positive integers `zero`, `one`, and `limit`.

A **binary arrayarr** is called **stable** if:

* The number of occurrences of `0` in `arr` is exactly `zero`.
* The number of occurrences of `1` in `arr` is exactly `one`.
* Each **subarray** of `arr` with a size greater than `limit` must contain both `0` and `1`.

Return the total number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1], as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.
```

**Example 2:**
```
Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Note that the binary arrays [1,1,0] and [0,1,1] have subarrays of length 2 with identical elements, hence, they are not stable.
```

**Example 3:**
```
Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].
```
 

**Constraints:**

* `1 <= zero, one, limit <= 200`

# Submissions
---
**Solution 1: (DP Bottom-Up, 3D DP)**
```
Runtime: 3956 ms
Memory: 22.54 MB
```
```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 7
        dp = [[[0] * 2 for _ in range(zero + 1)] for _ in range(one + 1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for m in range(one + 1):
            for n in range(zero + 1):
                for o in range(1, limit + 1):
                    if m - o >= 0:
                        dp[m][n][1] = (dp[m][n][1] + dp[m - o][n][0]) % M
                    if n - o >= 0:
                        dp[m][n][0] = (dp[m][n][0] + dp[m][n - o][1]) % M
        return (dp[one][zero][0] + dp[one][zero][1]) % M
```

**Solution 2: (DP Top-Down, 3D DP)**
```
Runtime: 242 ms, Beats 61.79%
Memory: 8.71 MB, Beats 84.55%
```
```c++
class Solution {
    int mod = 1e9 + 7; 
    int dp[202][202][2];    
    int dfs(int one, int zero, bool cur, int limit){
        if (one == 0 && zero == 0) {
            return 1;
        }
        if (dp[one][zero][cur] != -1) {
            return dp[one][zero][cur]; 
        }
        int rst = 0;
        if (cur == 1) {
            for (int k = 1; k <= min(one, limit); k ++) {
                rst = (rst + dfs(one - k, zero, 0, limit) % mod) % mod;
            }
        } else { 
            for (int k = 1; k <= min(zero, limit); k ++) {
                rst = (rst + dfs(one, zero - k, 1, limit) % mod) % mod;
            }
        }
        return dp[one][zero][cur] = rst % mod; 
    }
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        memset(dp, -1, sizeof(dp));
        int a = dfs(one, zero, 1, limit)%mod;
        int b = dfs(one, zero, 0, limit)%mod;
        return (a+b)%mod; 
    }
};
```

**Solution 3: (DP Top-Down, 3D DP, Sliding Window, state transition, constraint)**

dp[i][j][0] = number of valid arrays using i zeros and j ones, ending in 0

dp[i][j][1] = number of valid arrays using i zeros and j ones, ending in 1

        --zero-       -zero-

  -one-         -one-
        limit+1
        -------
    . 1 0 ... 0 1 ... 0 ....
        -----                          
        limit
          -----                      
          limit 
              ^dp[i][j][0] 
            ^dp[i-1][j][0] + dp[i-1][j][1]
      ^dp[i-limit-1][j][1]

    zero = 1, one = 1, limit = 2
dp  0   1    j
    0 1 0 1 
0   1 1   1
1   1   1 1
i       ^^^
        ans

    zero = 1, one = 2, limit = 1
dp  0   1   2
    0 1 0 1 0 1
0   1 1   1
1   1   1 1   1
            ^^^
            ans

    zero = 3, one = 3, limit = 2

dp  0   1   2   3     one
    0 1 0 1 0 1 0 1
0   1 1   1   1
1   1   1 1 1 2   2
2   1   2 1 3 3 2 5
3       2   5 2 7 7
zero            ^^^
                ans

```
Runtime: 115 ms, Beats 79.67%
Memory: 51.10 MB, Beats 34.15%
```
```c++
class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        vector<vector<vector<long long>>> dp(
            zero + 1, vector<vector<long long>>(one + 1, vector<long long>(2)));
        long long mod = 1e9 + 7;
        for (int i = 0; i <= min(zero, limit); i++) {
            dp[i][0][0] = 1;
        }
        for (int j = 0; j <= min(one, limit); j++) {
            dp[0][j][1] = 1;
        }
        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                if (i > limit) {
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1] -
                                  dp[i - limit - 1][j][1];
                } else {
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1];
                }
                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod;
                if (j > limit) {
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0] -
                                  dp[i][j - limit - 1][0];
                } else {
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0];
                }
                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod;
            }
        }
        return (dp[zero][one][0] + dp[zero][one][1]) % mod;
    }
};
```
