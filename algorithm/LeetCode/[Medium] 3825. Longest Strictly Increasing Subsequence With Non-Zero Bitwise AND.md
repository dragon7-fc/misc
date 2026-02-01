3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND

You are given an integer array `nums`.

Return the length of the **longest** strictly increasing **subsequence** in `nums` whose bitwise **AND** is non-zero. If no such subsequence exists, return `0`.

 

**Example 1:**
```
Input: nums = [5,4,7]

Output: 2

Explanation:

One longest strictly increasing subsequence is [5, 7]. The bitwise AND is 5 AND 7 = 5, which is non-zero.
```

**Example 2:**
```
Input: nums = [2,3,6]

Output: 3

Explanation:

The longest strictly increasing subsequence is [2, 3, 6]. The bitwise AND is 2 AND 3 AND 6 = 2, which is non-zero.
```

**Example 3:**
```
Input: nums = [0,1]

Output: 1

Explanation:

One longest strictly increasing subsequence is [1]. The bitwise AND is 1, which is non-zero.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up, LIS)**
```
Runtime: 396 ms, Beats 71.43%
Memory: 148.73 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size(), i, j, ans = 0;
        vector<int> dp;
        for (i = 0; i < 30; i ++) {
            for (j = 0; j < n; j ++) {
                if (nums[j] & (1 << i)) {
                    if (dp.empty() || dp.back() < nums[j]) {
                        dp.push_back(nums[j]);
                    } else {
                        auto it = lower_bound(begin(dp), end(dp), nums[j]);
                        *it = nums[j];
                    }
                }
                ans = max(ans, (int)dp.size());
            }
            dp.clear();
        }
        return ans;
    }
};
```
