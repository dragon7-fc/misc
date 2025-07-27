552. Student Attendance Record II

Given a positive integer **n**, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10^9 + 7.

A student attendance record is a string that only contains the following three characters:

1. '**A**' : Absent.
1. '**L**' : Late.
1. '**P**' : Present.

A record is regarded as rewardable if it doesn't contain **more than one 'A' (absent)** or **more than two continuous 'L' (late)**.

**Example 1:**
```
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
```

**Note:** The value of **n** won't exceed `100,000`.

# Submissions
---
**Solution 1: (DP Bottom-Up, state set)**
```
Runtime: 804 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9 + 7)
        XAXL = 1      # No A no L in the end
        XAL = 0       # No A with one L in the end 
        XALL = 0      # No A with two L in the end 
        AXL = 0       # One A no L in the end
        AL = 0        # One A with one L in the end
        ALL = 0       # One A with two L in the end
        for _ in range(1, n+1):
            N_XAXL = XAXL
            N_XAL = XAL
            N_XALL = XALL
            N_AXL = AXL
            N_AL = AL
            N_ALL = ALL

            ALL = N_AL
            AL = N_AXL
            XAL = N_XAXL
            XALL = N_XAL
            XAXL = (N_XAL + N_XALL + N_XAXL) % MOD;
            AXL = (N_AXL + N_AL + N_ALL + N_XAL + N_XALL + N_XAXL) % MOD;

        return (XAXL + XAL + XALL + AXL + AL + ALL) % MOD
```

**Solution 2: (Top-Down Dynamic Programming with Memoization)**
```
Runtime: 1506 ms
Memory: 399.12 MB
```
```c++
class Solution {
    int MOD = 1e9 + 7;
    // Cache to store sub-problem results.
    vector<vector<vector<int>>> memo;

public:
    // Recursive function to return the count of combinations of length 'n' eligible for the award.
    int eligibleCombinations(int n, int totalAbsences, int consecutiveLates) {
        // If the combination has become not eligible for the award,
        // then we will not count any combinations that can be made using it.
        if (totalAbsences >= 2 or consecutiveLates >= 3) {
            return 0;
        }
        // If we have generated a combination of length 'n' we will count it.
        if (n == 0) {
            return 1;
        }
        // If we have already seen this sub-problem earlier, we return the stored result.
        if (memo[n][totalAbsences][consecutiveLates] != -1) {
            return memo[n][totalAbsences][consecutiveLates];
        }

        int count = 0;
        // We choose 'P' for the current position.
        count = eligibleCombinations(n - 1, totalAbsences, 0);
        // We choose 'A' for the current position.
        count = (count + eligibleCombinations(n - 1, totalAbsences + 1, 0)) % MOD;
        // We choose 'L' for the current position.
        count = (count + eligibleCombinations(n - 1, totalAbsences, consecutiveLates + 1)) % MOD;

        // Return and store the current sub-problem result in the cache.
        return memo[n][totalAbsences][consecutiveLates] = count;
    }
public:
    int checkRecord(int n) {
       // Initialize the cache.
        memo = vector<vector<vector<int>>>(n + 1, vector<vector<int>>(2, vector<int>(3, -1)));
        // Return count of combinations of length 'n' eligible for the award.
        return eligibleCombinations(n, 0, 0);
    }
};
```

**Solution 3: (Bottom-Up Dynamic Programming)**
```
Runtime: 1097 ms
Memory: 386.75 MB
```
```c++
class Solution {
public:
    int checkRecord(int n) {
       int MOD = 1000000007;
        // Cache to store sub-problem results.
        vector<vector<vector<int>>> dp = vector<vector<vector<int>>>(n + 1, 
                                            vector<vector<int>>(2, vector<int>(3, 0)));

        // Base case: there is 1 string of length 0 with zero 'A' and zero 'L'.
        dp[0][0][0] = 1;

        // Iterate on smaller sub-problems and use the current smaller sub-problem 
        // to generate results for bigger sub-problems.
        for (int len = 0; len < n; ++len) {
            for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
                for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                    // Store the count when 'P' is chosen.
                    dp[len + 1][totalAbsences][0] = (
                        dp[len + 1][totalAbsences][0] +
                        dp[len][totalAbsences][consecutiveLates]
                    ) % MOD;
                    // Store the count when 'A' is chosen.
                    if (totalAbsences < 1) {
                        dp[len + 1][totalAbsences + 1][0] = (
                            dp[len + 1][totalAbsences + 1][0] + 
                            dp[len][totalAbsences][consecutiveLates]
                        ) % MOD;
                    }
                    // Store the count when 'L' is chosen.
                    if (consecutiveLates < 2) {
                        dp[len + 1][totalAbsences][consecutiveLates + 1] = (
                            dp[len + 1][totalAbsences][consecutiveLates + 1] + 
                            dp[len][totalAbsences][consecutiveLates]
                        ) % MOD;
                    }
                }
            }
        }

        // Sum up the counts for all combinations of length 'n' with different absent and late counts.
        int count = 0;
        for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
            for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                count = (count + dp[n][totalAbsences][consecutiveLates]) % MOD;
            }
        }
        return count;
    }
};
```

**Solution 4: (Bottom-Up Dynamic Programming, Space Optimized)**
```
Runtime: 1720 ms
Memory: 420.22 MB
```
```c++
class Solution {
public:
    int checkRecord(int n) {
        int MOD = 1000000007;
        // Cache to store current sub-problem results.
        vector<vector<int>> dpCurrState = vector<vector<int>>(2, vector<int>(3, 0));
        // Cache to store next sub-problem results.
        vector<vector<int>> dpNextState = vector<vector<int>>(2, vector<int>(3, 0));

        // Base case: there is 1 string of length 0 with zero 'A' and zero 'L'.
        dpCurrState[0][0] = 1;

        // Iterate on smaller sub-problems and use the current smaller sub-problem 
        // to generate results for bigger sub-problems.
        for (int len = 0; len < n; ++len) {
            for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
                for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                    // Store the count when 'P' is chosen.
                    dpNextState[totalAbsences][0] = (
                        dpNextState[totalAbsences][0] + 
                        dpCurrState[totalAbsences][consecutiveLates]
                    ) % MOD;
                    // Store the count when 'A' is chosen.
                    if (totalAbsences < 1) {
                        dpNextState[totalAbsences + 1][0] = (
                            dpNextState[totalAbsences + 1][0] + 
                            dpCurrState[totalAbsences][consecutiveLates]
                        ) % MOD;
                    }
                    // Store the count when 'L' is chosen.
                    if (consecutiveLates < 2) {
                        dpNextState[totalAbsences][consecutiveLates + 1] = (
                            dpNextState[totalAbsences][consecutiveLates + 1] + 
                            dpCurrState[totalAbsences][consecutiveLates]
                        ) % MOD;
                    }
                }
            }
            
            // Next state sub-problems will become current state sub-problems in next iteration.
            dpCurrState = dpNextState;
            // Next state sub-problem results will reset to zero.
            dpNextState = vector<vector<int>>(2, vector<int>(3, 0));
        }

        // Sum up the counts for all combinations of length 'n' with different absent and late counts.
        int count = 0;
        for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
            for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                count = (count + dpCurrState[totalAbsences][consecutiveLates]) % MOD;
            }
        }
        return count;
    }
};
```

**Solution 5: (DP Top-Down)**
```
Runtime: 278 ms
Memory: 17.52 MB
```
```c++
class Solution {
    int mod = 1e9 + 7;
    int dp[100001][2][3];
    int dfs(int i, int a, int l) {
        if (a >= 2 || l >= 3) {
            return 0;
        }
        if (i == 0) {
            return 1;
        }
        if (dp[i][a][l] != -1) {
            return dp[i][a][l];
        }
        int rst = dfs(i-1, a, 0) % mod;
        rst = (rst + dfs(i-1, a+1, 0)) % mod;
        rst = (rst + dfs(i-1, a, l+1)) % mod;
        dp[i][a][l] = rst;
        return rst;
    }
public:
    int checkRecord(int n) {
        memset(dp, -1, sizeof(dp));
        return dfs(n, 0, 0);
    }
};
```

**Solution 6: (DP Bottom-Up)**
```
Runtime: 7 ms, Beats 98.92%
Memory: 7.81 MB, Beats 97.53%
```
```c++
class Solution {
public:
    int checkRecord(int n) {
        int i, MOD = 1e9 + 7;
        long long pxa = 1, pxal = 1, pxall = 0, pa = 1, pal = 0, pall = 0, xa, xal, xall, a, al, all;
        for (i = 1; i < n; i ++) {
            xa = (pxa + pxal + pxall) % MOD;
            xal = pxa;
            xall = pxal;
            a = (pxa + pxal + pxall + pa + pal + pall) % MOD;
            al = pa;
            all = pal;

            pxa = xa;
            pxal = xal;
            pxall = xall;
            pa = a;
            pal = al;
            pall = all;
        }
        return (pxa + pxal + pxall + pa + pal + pall) % MOD;
    }
};
```
