3780. Maximum Sum of Three Numbers Divisible by Three

You are given an integer array `nums`.

Your task is to choose exactly three integers from `nums` such that their sum is divisible by three.

Return the maximum possible sum of such a triplet. If no such triplet exists, return 0.

 

**Example 1:**
```
Input: nums = [4,2,3,1]

Output: 9

Explanation:

The valid triplets whose sum is divisible by 3 are:

(4, 2, 3) with a sum of 4 + 2 + 3 = 9.
(2, 3, 1) with a sum of 2 + 3 + 1 = 6.
Thus, the answer is 9.
```

**Example 2:**
```
Input: nums = [2,1,5]

Output: 0

Explanation:

No triplet forms a sum divisible by 3, so the answer is 0.
```
 

**Constraints:**

* `3 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 106 ms, Beats 16.67%
Memory: 289.76 MB, Beats 8.33%
```
```c++
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        vector<vector<int>> dp(3);
        sort(nums.begin(), nums.end(), greater<>());
        for (auto &num: nums) {
            dp[num % 3].push_back(num);
        }
        int ans = 0;
        if (dp[0].size() >= 3) {
            ans = max(ans, dp[0][0] + dp[0][1] + dp[0][2]);
        }
        if (dp[1].size() >= 3) {
            ans = max(ans, dp[1][0] + dp[1][1] + dp[1][2]);
        }
        if (dp[2].size() >= 3) {
            ans = max(ans, dp[2][0] + dp[2][1] + dp[2][2]);
        }
        if (dp[0].size() && dp[1].size() && dp[2].size()) {
            ans = max(ans, dp[0][0] + dp[1][0] + dp[2][0]);
        }
        return ans;
    }
};
```
