3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array `nums` and a positive integer `k`. A **subsequence** `sub` of `nums` with length `x` is called **valid** if it satisfies:

* `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k`.

Return the length of the **longest valid** subsequence of `nums`.
 

**Example 1:**
```
Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].
```

**Example 2:**
```
Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].
```
 

**Constraints:**

* `2 <= nums.length <= 10^3`
* `1 <= nums[i] <= 10^7`
* `1 <= k <= 10^3`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 67 ms
Memory: 128.88 MB
```
```c++
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> dp(k, vector<int>(k, 0));
        int maxLen = 0;
        
        for (int num : nums) {
            for (int j = 0; j < k; ++j) {
                int remainder = num % k;
                maxLen = max(maxLen, dp[remainder][j] = dp[j][remainder] + 1);
            }
        }
        
        return maxLen;
    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 111 ms, Beats 55.75%
Memory: 90.15 MB, Beats 71.68%
```
```c++
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size(), i, j, a, ans = 0;
        vector<vector<int>> dp(n, vector<int>(k, 1));
        for (j = 1; j < n; j ++) {
            for (i = 0; i < j; i ++) {
                a = (nums[i] + nums[j])%k;
                dp[j][a] = max(dp[j][a], 1 + dp[i][a]);
                ans = max(ans, dp[j][a]);
            }
        }
        return ans;
    }
};
```
