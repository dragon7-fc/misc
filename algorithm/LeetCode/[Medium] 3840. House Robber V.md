3840. House Robber V

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.

You are given two integer arrays `nums` and `colors`, both of length `n`, where `nums[i]` is the amount of money in the `i`th house and `colors[i]` is the color code of that house.

You **cannot rob two adjacent** houses if they share the **same color** code.

Return the **maximum** amount of money you can rob.

 

**Example 1:**
```
Input: nums = [1,4,3,5], colors = [1,1,2,2]

Output: 9

Explanation:

Choose houses i = 1 with nums[1] = 4 and i = 3 with nums[3] = 5 because they are non-adjacent.
Thus, the total amount robbed is 4 + 5 = 9.
```

**Example 2:**
```
Input: nums = [3,1,2,4], colors = [2,3,2,2]

Output: 8

Explanation:

Choose houses i = 0 with nums[0] = 3, i = 1 with nums[1] = 1, and i = 3 with nums[3] = 4.
This selection is valid because houses i = 0 and i = 1 have different colors, and house i = 3 is non-adjacent to i = 1.
Thus, the total amount robbed is 3 + 1 + 4 = 8.
```

**Example 3:**
```
Input: nums = [10,1,3,9], colors = [1,1,1,2]

Output: 22

Explanation:

Choose houses i = 0 with nums[0] = 10, i = 2 with nums[2] = 3, and i = 3 with nums[3] = 9.
This selection is valid because houses i = 0 and i = 2 are non-adjacent, and houses i = 2 and i = 3 have different colors.
Thus, the total amount robbed is 10 + 3 + 9 = 22.
```

**Constraints:**

* `1 <= n == nums.length == colors.length <= 10^5`
* `1 <= nums[i], colors[i] <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 17 ms, Beats 26.09%
Memory: 235.08 MB, Beats 8.70%
```
```c++
class Solution {
public:
    long long rob(vector<int>& nums, vector<int>& colors) {
        int n = nums.size(), i;
        vector<long long> pre(2), dp(2);
        pre[0] = nums[0];
        for (i = 1; i < n; i ++) {
            if (colors[i] != colors[i - 1]) {
                dp[0] = pre[0] + nums[i];
            } else {
                dp[0] = max(pre[0], pre[1] + nums[i]);
            }
            dp[1] = max(pre[0], pre[1]);
            pre = dp;
        }
        return max(pre[0], pre[1]);
    }
};
```

**Solution 2: (DP Bottom-Up)**

Intuition
This problem is a variant of the House Robber problem.
We use Dynamic Programming to solve it.

Explanation
The goal is to maximize the stolen money.
We use Dynamic Programming to solve it.
dp2 is the max profit up to house i-1.
dp1 is the max profit up to house i-2.

If adjacent houses have the same color:
You cannot rob both at the same time.
Choose the max of skipping or robbing.
next_dp2 = max(dp2, dp1 + nums[i])

If adjacent houses have different colors:
The restriction does not apply to them.
You can rob both current and previous.
next_dp2 = dp2 + nums[i]

Complexity
Time O(n)
Space O(1)

    nums   = [ 1, 4, 3, 5], 
    colors = [ 1, 1, 2, 2]
dp1            0  1  4  7
dp2            1  4  7  9 < ans
next_dp2          4  7  9

```
Runtime: 4 ms, Beats 82.61%
Memory: 234.84 MB, Beats 8.70%
```
```c++
class Solution {
public:
    long long rob(vector<int>& nums, vector<int>& colors) {
        long long dp1 = 0, dp2 = nums[0], next_dp2;
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if (colors[i] == colors[i - 1]) {
                next_dp2 = max(dp2, dp1 + nums[i]);
            } else {
                next_dp2 = dp2 + nums[i];
            }
            dp1 = dp2;
            dp2 = next_dp2;
        }
        return dp2;
    }
};
```
