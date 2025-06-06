Find Sum of Array Product of Magical Sequences

You are given two integers, `m` and `k`, and an integer array `nums`.

A sequence of integers `seq` is called **magical** if:
* `seq` has a size of `m`.
* `0 <= seq[i] < nums.length`
* The **binary representation** of `2^seq[0] + 2^seq[1] + ... + 2^seq[m - 1]` has `k` **set bits**.

The **array product** of this sequence is defined as `prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]])`.

Return the **sum** of the **array products** for all valid **magical** sequences.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **set bit** refers to a bit in the binary representation of a number that has a value of 1.

 

**Example 1:**
```
Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

Output: 991600007

Explanation:

All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.
```

**Example 2:**
```
Input: m = 2, k = 2, nums = [5,4,3,2,1]

Output: 170

Explanation:

The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].
```

**Example 3:**
```
Input: m = 1, k = 1, nums = [28]

Output: 28

Explanation:

The only magical sequence is [0].
```
 

**Constraints:**

* `1 <= k <= m <= 30`
* `1 <= nums.length <= 50`
* `1 <= nums[i] <= 10^8`

# Submissions
---
**Solution 1: (Generating Function + 4D DP)**
```
Runtime: 126 ms, Beats 43.69%
Memory: 92.10 MB, Beats 23.30%
```
```c++
class Solution {
    long long modPow(long long a, long long e, int mod) {
        long long res = 1;
        while (e > 0) {
            if (e & 1) res = res * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return res;
    }
public:
    int magicalSum(int m, int k, vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();

        vector<long long> f(m + 1), inverse_f(m + 1);
        f[0] = 1;
        for (int i = 1; i <= m; i++) {
            f[i] = f[i - 1] * i % MOD;
        }

        inverse_f[m] = modPow(f[m], MOD - 2, MOD);
        for (int i = m; i >= 1; i--) {
            inverse_f[i - 1] = inverse_f[i] * i % MOD;
        }

        vector<vector<long long>> pow_nums(n, vector<long long>(m + 1, 1));
        for (int i = 0; i < n; i++) {
            for (int c = 1; c <= m; c++) {
                pow_nums[i][c] = pow_nums[i][c - 1] * nums[i] % MOD;
            }
        }

        vector dp(n + 1, vector(m + 1, vector(k + 1, vector<long long>(m + 1))));
        dp[0][0][0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int m1 = 0; m1 <= m; m1++) {
                for (int k1 = 0; k1 <= k; k1++) {
                    for (int m2 = 0; m2 <= m; m2++) {
                        long long val = dp[i][m1][k1][m2];
                        if (!val) continue;
                        for (int c = 0; c <= m - m1; c++) {
                            int m12 = m1 + c;
                            int s = c + m2;
                            int bit = s & 1;
                            int k2 = k1 + bit;
                            if (k2 > k) continue;
                            int m22 = s >> 1;
                            dp[i + 1][m12][k2][m22] = (dp[i + 1][m12][k2][m22] + val * inverse_f[c] % MOD * pow_nums[i][c] % MOD) % MOD;
                        }
                    }
                }
            }
        }

        long long ans = 0;
        for (int k1 = 0; k1 <= k; k1++) {
            for (int m2 = 0; m2 <= m; m2++) {
                long long val = dp[n][m][k1][m2];
                if (!val) continue;
                int bits = __builtin_popcount(m2);
                if (k1 + bits == k) {
                    ans = (ans + val) % MOD;
                }
            }
        }

        ans = ans * f[m] % MOD;
        return (int)ans;
    }
};
```
