3409. Longest Subsequence With Decreasing Adjacent Difference

You are given an array of integers `nums`.

Your task is to find the length of the **longest subsequence** `seq` of `nums`, such that the **absolute differences** between consecutive elements form a **non-increasing** sequence of integers. In other words, for a subsequence `seq0`, `seq1`, `seq2`, ..., `seqm` of `nums`, `|seq1 - seq0| >= |seq2 - seq1| >= ... >= |seqm - seqm - 1|`.

Return the length of such a subsequence.

A **subsequence** is an **non-empty** array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [16,6,3]

Output: 3

Explanation: 

The longest subsequence is [16, 6, 3] with the absolute adjacent differences [10, 3].
```

**Example 2:**
```
Input: nums = [6,5,3,4,2,1]

Output: 4

Explanation:

The longest subsequence is [6, 4, 2, 1] with the absolute adjacent differences [2, 2, 1].
```

**Example 3:**
```
Input: nums = [10,20,10,19,10,20]

Output: 5

Explanation: 

The longest subsequence is [10, 20, 10, 19, 10] with the absolute adjacent differences [10, 10, 9, 9].
```
 

**Constraints:**

* `2 <= nums.length <= 10^4`
* `1 <= nums[i] <= 300`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

       6,  5,  3,  4,  2,  1
      -----------------------
       ^           ^   ^   ^
dp     0 1 2 3  diff
    0  
    1  1 1 1
    2    2 2
    3
    4      3
    5
    6      4
   num

```
Runtime: 411 ms
Memory: 339.79 MB
```
```c++
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        vector<vector<int>> dp(302, vector<int>(302));

        for (int i = nums.size() - 1; i >= 0; --i){
            int num = nums[i];
    
            for (int next = 1; next <= 300; ++next){
                int diff = abs(next - num);
                dp[num][diff] = max(dp[num][diff], dp[next][diff] + 1);
            }

            for (int j = 1; j <= 300; ++j){
                dp[num][j] = max(dp[num][j], dp[num][j - 1]);
            }
        }

        int ans = INT_MIN;
        for (int i = 0; i <= 301; ++i){
            for (int j = 0; j <= 301; ++j){
                ans = max(ans, dp[i][j]);
            }
        }

        return ans;
    }
};
```
