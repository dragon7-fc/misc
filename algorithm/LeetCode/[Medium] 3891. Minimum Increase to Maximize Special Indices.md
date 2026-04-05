3891. Minimum Increase to Maximize Special Indices

You are given an integer array nums of length `n`.

An index `i (0 < i < n - 1)` is **special** if `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`.

You may perform operations where you choose any index `i` and increase `nums[i]` by 1.

Your goal is to:

* **Maximize** the number of **special** indices.
* **Minimize** the total number of operations required to achieve that **maximum**.

Return an integer denoting the **minimum** total number of operations required.

 

**Example 1:**
```
Input: nums = [1,2,2]

Output: 1

Explanation:

Start with nums = [1, 2, 2].
Increase nums[1] by 1, array becomes [1, 3, 2].
The final array is [1, 3, 2] has 1 special index, which is the maximum achievable.
It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.
```

**Example 2:**
```
Input: nums = [2,1,1,3]

Output: 2

Explanation:

Start with nums = [2, 1, 1, 3].
Perform 2 operations at index 1, array becomes [2, 3, 1, 3].
The final array is [2, 3, 1, 3] has 1 special index, which is the maximum achievable. Thus, the answer is 2.
```

**Example 3:**
```
Input: nums = [5,2,1,4,3]

Output: 4

Explanation:

Start with nums = [5, 2, 1, 4, 3].
Perform 4 operations at index 1, array becomes [5, 6, 1, 4, 3].
The final array is [5, 6, 1, 4, 3] has 2 special indices, which is the maximum achievable. Thus, the answer is 4.
```

**Constraints:**

* `3 <= n <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up, level by level)**
```
Runtime: 8 ms, Beats 79.59%
Memory: 150.83 MB, Beats 68.91%
```
```c++
class Solution {
public:
    long long minIncrease(vector<int>& nums) {
        int n = nums.size(), i;
        vector<long long> dp(n);
        long long ans;
        for (i = 1; i < n - 1; i ++) {
            if (i % 2) {
                dp[i + 1] = dp[i - 1] + max(max(nums[i - 1], nums[i + 1]) + 1 - nums[i], 0);
            } else {
                dp[i + 1] = min(dp[i], dp[i - 1] + max(max(nums[i - 1], nums[i + 1]) + 1 - nums[i], 0));
            }
        }
        return dp.back();
    }
};
```
