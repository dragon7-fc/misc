3176. Find the Maximum Length of a Good Subsequence I

You are given an integer array `nums` and a non-negative integer `k`. A sequence of integers `seq` is called **good** if there are at most `k` indices i in the range `[0, seq.length - 2]` such that `seq[i] != seq[i + 1]`.

Return the maximum possible length of a **good** subsequence of `nums`.

 

**Example 1:**
```
Input: nums = [1,2,1,1,3], k = 2

Output: 4

Explanation:

The maximum length subsequence is [1,2,1,1,3].
```

**Example 2:**
```
Input: nums = [1,2,3,4,5,1], k = 0

Output: 2

Explanation:

The maximum length subsequence is [1,2,3,4,5,1].
```
 

**Constraints:**

* `1 <= nums.length <= 500`
* `1 <= nums[i] <= 10^9`
* `0 <= k <= min(nums.length, 25)`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 82 ms
Memory: 20.86 MB
```
```c++
class Solution {
    int dp[500][26];
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size(), ans = 1;
        for (int i = 0; i < n; i ++) {
            dp[i][0] = 1;
        }
        for (int j = 1; j < n; j ++) {
            for (int i = 0; i < j; i ++) {
                if (nums[i] == nums[j]) {
                    for (int ck = 0; ck <= k; ck++) {
                        dp[j][ck] = max(dp[j][ck], dp[i][ck] + 1);
                        ans = max(ans, dp[j][ck]);
                    }
                } else {
                    for (int ck = 0; ck < k; ck++) {
                        dp[j][ck+1] = max(dp[j][ck+1], dp[i][ck] + 1);
                        ans = max(ans, dp[j][ck+1]);
                    }
                }
            }
        }
        return ans;
    }
};
```
