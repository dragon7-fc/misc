2289. Steps to Make Array Non-decreasing

You are given a **0-indexed** integer array `nums`. In one step, remove all elements `nums[i]` where `nums[i - 1] > nums[i]` for all `0 < i < nums.length`.

Return the number of steps performed until `nums` becomes a **non-decreasing** array.

 

**Example 1:**
```
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
```

**Example 2:**
```
Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Stack, DP)**

dp[i] means the number of element A[i] can eat.

Iterative input array A reversely,
If A[i] is bigger the head element A[j] of stack,
this means A[i] can eat that element,
Then update dp[i] to be max of dp[i] + 1 and dp[j].

```
Runtime: 1568 ms
Memory Usage: 28.6 MB
```
```python
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                res = max(res, dp[i])
            stack.append(i)
        return res
```

**Solution 2: (Stack, DP)**
```
Runtime: 292 ms
Memory Usage: 78.1 MB
```
```c++
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size(), res = 0;
        vector<int> stack, dp(n);
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.empty() && nums[i] > nums[stack.back()]) {
                dp[i] = max(++dp[i], dp[stack.back()]);
                stack.pop_back();
                res = max(res, dp[i]);
            }
            stack.push_back(i);
        }
        return res;
    }
};
```
