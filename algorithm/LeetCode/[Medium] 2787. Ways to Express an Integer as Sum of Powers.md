2787. Ways to Express an Integer as Sum of Powers

Given two positive integers `n` and `x`.

Return the number of ways `n` can be expressed as the sum of the `x`th power of unique positive integers, in other words, the number of sets of unique integers `[n1, n2, ..., nk]` where `n = n1^x + n2^x + ... + nk^x`.

Since the result can be very large, return it modulo `10^9 + 7`.

For example, if `n = 160` and `x = 3`, one way to express n is `n = 2^3 + 3^3 + 5^3`.

 

**Example 1:**
```
Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
```

**Example 2:**
```
Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
```

**Constraints:**

* `1 <= n <= 300`
* `1 <= x <= 5`

# Submissions
---
**Solution 1: (DP Top-Down, taken and not_taken)**
```
Runtime: 610 ms
Memory: 11.1 MB
```
```c++
class Solution {
    long long dp[301][301][6] = {};
    long long dfs(int i, int n, int x) {
        if (pow(i, x) > n)
            return n == 0;
        if (dp[i][n][x] == 0)
            dp[i][n][x] = 1 + dfs(i + 1, n - pow(i, x), x) + dfs(i + 1, n, x);
        return dp[i][n][x] - 1;
    }
public:
    int numberOfWays(int n, int x) {
        return dfs(1, n, x) % 1000000007;
    }
};
```
