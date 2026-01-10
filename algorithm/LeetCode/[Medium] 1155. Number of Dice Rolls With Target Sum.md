1155. Number of Dice Rolls With Target Sum

You have `d` dice, and each die has `f` faces numbered `1, 2, ..., f`.

Return the number of possible ways (out of $f^d$ total ways) **modulo** `10^9 + 7` to roll the dice so the sum of the face up numbers equals `target`.

 

**Example 1:**

```
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
```

**Example 2:**

```
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

**Example 3:**

```
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
```

**Example 4:**

```
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
```

**Example 5:**

```
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
```

**Constraints:**

* `1 <= d, f <= 30`
* `1 <= target <= 1000`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 296 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f:
            return 0
        
        dp = [[0]*target for _ in range(d)]
        
        for j in range(f):
            if j < target:
                dp[0][j] = 1
        
        for i in range(1, d):
            for j in range(target):
                for k in range(f):
                    if j-k > 0:
                        dp[i][j] += dp[i-1][j-k-1]
                        dp[i][j] %= 1000000007
        
        return dp[d-1][target-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 416 ms
Memory Usage: 21 MB
```
```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9 + 7
        
        @functools.lru_cache(None)
        def dp(n, t):
            if n == 0:
                if t != 0:
                    return 0
                else:
                    return 1
            return sum([dp(n-1, t-i) for i in range(1, f+1)])
        
        return dp(d, target) % MOD
```

**solution 3: (DP Bottom-Up)**
```
Runtime: 29 ms
Memory: 6.6 MB
```
```c++
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int MOD = 1e9 + 7;
        int dp[target+1][n+1];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int t = 1; t <= target; t ++) {
            for (int i = 1; i <= n; i ++) {
                for (int j = 1; j <= k; j ++) {
                    if (t-j >= 0) {
                        dp[t][i] = (dp[t][i] + dp[t-j][i-1]) % MOD;
                    }
                }
            }
        }
        return dp[target][n];
    }
};
```

**solution 4: (DP Bottom-Up)**
```
Runtime: 8 ms
Memory: 6.5 MB
```
```c++
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int MOD = 1e9 + 7;
        int dp[n+1][target+1];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= min(i*k, target); j++) {
                for (int f = 1; f <= min(k, j); f++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j-f]) % MOD;
                }
            }
        }
        return dp[n][target];
    }
};
```

**Solution 5: (DP Bottom-Up 1D)**
```
Runtime: 7 ms
Memory: 7.2 MB
```
```c++
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int MOD = 1e9 + 7;
        int dp[n+1][target+1];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= min(i*k, target); j++) {
                for (int f = 1; f <= min(k, j); f++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j-f]) % MOD;
                }
            }
        }
        return dp[n][target];
    }
};
```
