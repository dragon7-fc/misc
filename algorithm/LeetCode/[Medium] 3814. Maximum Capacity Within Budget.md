3814. Maximum Capacity Within Budget

You are given two integer arrays `costs` and `capacity`, both of length `n`, where `costs[i]` represents the purchase cost of the `i`th machine and `capacity[i]` represents its performance capacity.

You are also given an integer `budget`.

You may select **at most two distinct** machines such that the total cost of the selected machines is strictly less than `budget`.

Return the **maximum** achievable total capacity of the selected machines.

 

**Example 1:**
```
Input: costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8

Output: 8

Explanation:

Choose two machines with costs[0] = 4 and costs[3] = 3.
The total cost is 4 + 3 = 7, which is strictly less than budget = 8.
The maximum total capacity is capacity[0] + capacity[3] = 1 + 7 = 8.
```

**Example 2:**
```
Input: costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7

Output: 6

Explanation:

Choose one machine with costs[3] = 4.
The total cost is 4, which is strictly less than budget = 7.
The maximum total capacity is capacity[3] = 6.
```

**Example 3:**
```
Input: costs = [2,2,2], capacity = [3,5,4], budget = 5

Output: 9

Explanation:

Choose two machines with costs[1] = 2 and costs[2] = 2.
The total cost is 2 + 2 = 4, which is strictly less than budget = 5.
The maximum total capacity is capacity[1] + capacity[2] = 5 + 4 = 9.
```

**Constraints:**

* `1 <= n == costs.length == capacity.length <= 10^5`
* `1 <= costs[i], capacity[i] <= 10^5`
* `1 <= budget <= 2 * 10^5`

# Submissions
---
**Solution 1: (Sort, Prefix Sum, Two Pointers)**
```
Runtime: 59 ms, Beats 99.04%
Memory: 258.50 MB, Beats 85.89%
```
```c++
class Solution {
public:
    int maxCapacity(vector<int>& costs, vector<int>& capacity, int budget) {
        int n = costs.size(), i, j, j0, c, k, ans = 0;
        vector<long long> dp(n);
        for (i = 0; i < n; ++i) {
            dp[i] = (long long)costs[i] << 32 | capacity[i];
        }
        sort(dp.begin(), dp.end());
        j = n - 1;
        vector<int> pre(n);
        for (i = 0; i < n; ++i) {
            c = dp[i] >> 32;
            k = (int)dp[i];
            if (i == 0) {
                pre[i] = k;
            } else {
                pre[i] = max(pre[i - 1], k);
            }
            if (c < budget) {
                ans = max(ans, k);
            }
            while (j >= 0 && (dp[j] >> 32) + c >= budget) {
                j -= 1;
            }
            j0 = min(j, i - 1);
            if (j0 >= 0) {
                ans = max(ans, k + pre[j0]);
            }
        }
        return ans;
    }
};
```
