3693. Climbing Stairs II

You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

You are also given a **1-indexed** integer array `costs` of length `n`, where `costs[i]` is the cost of step `i`.

From step `i`, you can jump only to step `i + 1`, `i + 2`, or `i + 3`. The cost of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)^2`

You start from step 0 with `cost = 0`.

Return the minimum total cost to reach step `n`.

 

**Example 1:**
```
Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

Jump	Cost Calculation	Cost
0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
Thus, the minimum total cost is 2 + 3 + 8 = 13
```

**Example 2:**
```
Input: n = 4, costs = [5,1,6,2]

Output: 11

Explanation:

One optimal path is 0 → 2 → 4

Jump	Cost Calculation	Cost
0 → 2	costs[2] + (2 - 0)2 = 1 + 4	5
2 → 4	costs[4] + (4 - 2)2 = 2 + 4	6
Thus, the minimum total cost is 5 + 6 = 11
```

**Example 3:**
```
Input: n = 3, costs = [9,8,3]

Output: 12

Explanation:

The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)2 = 3 + 9 = 12
```
 

**Constraints:**

* `1 <= n == costs.length <= 10^5`
* `1 <= costs[i] <= 10^4`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 17 ms, Beats 37.50%
Memory: 177.54 MB, Beats 96.48%
```
```c++
class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        int i, j;
        costs.insert(costs.begin(), 0);
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (i = 1; i <= n; i ++) {
            for (j = i-1; j >= 0 && i - j <= 3; j --) {
                dp[i] = min(dp[i], dp[j] + costs[i] + (i - j) * (i - j));
            }
        }
        return dp.back();

    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 12 ms, Beats 80.13%
Memory: 169.64 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        vector<int> dp(3);
        for (int i = 1; i <= n; i++) {
            int best = INT_MAX;
            if (i >= 1) best = min(best, dp[(i - 1) % 3] + 1);
            if (i >= 2) best = min(best, dp[(i - 2) % 3] + 4);
            if (i >= 3) best = min(best, dp[(i - 3) % 3] + 9);
            dp[i % 3] = best + costs[i - 1];
        }
        return dp[n % 3];
    }
};
```
