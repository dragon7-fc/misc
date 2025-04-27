3205. Maximum Array Hopping Score I

Given an array `nums`, you have to get the **maximum** score starting from index `0` and hopping until you reach the last element of the array.

In each hop, you can jump from index `i` to an index `j > i`, and you get a score of `(j - i) * nums[j]`.

Return the maximum score you can get.

 

**Example 1:**
```
Input: nums = [1,5,8]

Output: 16

Explanation:

There are two possible ways to reach the last element:

0 -> 1 -> 2 with a score of (1 - 0) * 5 + (2 - 1) * 8 = 13.
0 -> 2 with a score of (2 - 0) * 8 = 16.
```

**Example 2:**
```
Input: nums = [4,5,2,8,9,1,3]

Output: 42

Explanation:

We can do the hopping 0 -> 4 -> 6 with a score of (4 - 0) * 9 + (6 - 4) * 3 = 42.
```
 

**Constraints:**

`2 <= nums.length <= 10^3`
`1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 105 ms, Beats 47.50%
Memory: 31.55 MB, Beats 80.00%
```
```c++
class Solution {
public:
    int maxScore(vector<int>& nums) {
        int n = nums.size(), i, j;
        vector<int> dp(n);
        for (j = 1; j < n; j ++) {
            for (i = 0; i < j; i ++) {
                dp[j] = max(dp[j], dp[i] + (j-i)*nums[j]);
            }
        }
        return dp[n-1];
    }
};
```

**Solution 2: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 31.24 MB, Beats 87.50%
```
```c++
class Solution {
public:
    int maxScore(vector<int>& nums) {
        int ans = 0, cur = 0;
        for (int i = nums.size() - 1; i > 0; i--) {
            cur = max(nums[i], cur);
            ans += cur;
        }
        return ans;
    }
```
