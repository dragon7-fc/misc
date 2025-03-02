3469. Find Minimum Cost to Remove Array Elements

You are given an integer array `nums`. Your task is to remove all elements from the array by performing one of the following operations at each step until `nums` is empty:

* Choose any two elements from the first three elements of `nums` and remove them. The cost of this operation is the **maximum** of the two elements removed.
* If fewer than three elements remain in nums, remove all the remaining elements in a single operation. The cost of this operation is the **maximum** of the remaining elements.

Return the **minimum** cost required to remove all the elements.

 

**Example 1:**
```
Input: nums = [6,2,8,4]

Output: 12

Explanation:

Initially, nums = [6, 2, 8, 4].

In the first operation, remove nums[0] = 6 and nums[2] = 8 with a cost of max(6, 8) = 8. Now, nums = [2, 4].
In the second operation, remove the remaining elements with a cost of max(2, 4) = 4.
The cost to remove all elements is 8 + 4 = 12. This is the minimum cost to remove all elements in nums. Hence, the output is 12.
```

**Example 2:**
```
Input: nums = [2,1,3,3]

Output: 5

Explanation:

Initially, nums = [2, 1, 3, 3].

In the first operation, remove nums[0] = 2 and nums[1] = 1 with a cost of max(2, 1) = 2. Now, nums = [3, 3].
In the second operation remove the remaining elements with a cost of max(3, 3) = 3.
The cost to remove all elements is 2 + 3 = 5. This is the minimum cost to remove all elements in nums. Hence, the output is 5.
```
 

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (DP Top-Down, Pick all three possible way)**

hard to braw bottom-up dp
-> change to top-down dp

    x x x x x x
    ^   ^ ^
    pi  i i+1
            ^
            i+2
dp[i][pi] = min(
    max(nums[i], nums[pi]) + dp(i+2, i+1)
    max(nums[i], nums[i+1] + dp(i+2, pi)
    max(nums[i+1], nums[pi]) + dp(i+2, i+1)
)

```
Runtime: 254 ms, Beats 23.53%
Memory: 181.76 MB, Beats 29.41%
```
```c++
class Solution {
    int dfs(int i, int pi, vector<vector<int>> &dp, vector<int> &nums) {
        if (i+1 >= nums.size()) {
            return max(nums[pi], i < nums.size() ? nums[i] : 0);
        }
        if (dp[i][pi] != -1) {
            return dp[i][pi];
        }
        int rst = max(nums[i], nums[i+1]) + dfs(i+2, pi, dp, nums);
        rst = min(rst, max(nums[i], nums[pi]) + dfs(i+2, i+1, dp, nums));
        rst = min(rst, max(nums[i+1], nums[pi]) + dfs(i+2, i, dp, nums));
        dp[i][pi] = rst;
        return rst;
    }
public:
    int minCost(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return dfs(1, 0, dp, nums);
    }
};
```
