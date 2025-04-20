3183. The Number of Ways to Make the Sum

You have an infinite number of coins with values 1, 2, and 6, and **only** 2 coins with value 4.

Given an integer n, return the number of ways to make the sum of `n` with the coins you have.

Since the answer may be very large, return it modulo `10^9 + 7`.

Note that the order of the coins doesn't matter and `[2, 2, 3]` is the same as `[2, 3, 2]`.

 

**Example 1:**
```
Input: n = 4

Output: 4

Explanation:

Here are the four combinations: [1, 1, 1, 1], [1, 1, 2], [2, 2], [4].
```

**Example 2:**
```
Input: n = 12

Output: 22

Explanation:

Note that [4, 4, 4] is not a valid combination since we cannot use 4 three times.
```

**Example 3:**
```
Input: n = 5

Output: 4

Explanation:

Here are the four combinations: [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 4].
```
 

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 121 ms, Beats 41.18%
Memory: 57.30 MB, Beats 76.47%
```
```c++
class Solution {
public:
    int numberOfWays(int n) {
        int coins[] = {1, 2, 6}, MOD = 1e9 + 7;
        vector<int> dp(n + 1);
        dp[0] = 1; // 1 way to form amount = 0.
        if (n >= 4) {
            dp[4] = 1;
        }
        if (n >= 8) {
            dp[8] = 1;
        }
        for (int coin: coins) {
            for (int i = 1; i <= n; i ++){
                if (coin > i) {
                    continue;
                }
                dp[i] += (dp[i-coin]) % MOD; // induction rule. dp[i] = ways to form amount with coin.
            }
        }
        return dp[n];
    }
};
```
