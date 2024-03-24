1856. Maximum Subarray Min-Product

The **min-product** of an array is equal to the **minimum value** in the array **multiplied** by the array's sum.

* For example, the array `[3,2,5]` (minimum value `is 2)` has a min-product of `2 * (3+2+5) = 2 * 10 = 20`.

Given an array of integers `nums`, return the **maximum min-product** of any **non-empty subarray** of `nums`. Since the answer may be large, return it **modulo** `10^9 + 7`.

Note that the min-product should be maximized **before** performing the modulo operation. Testcases are generated such that the maximum min-product **without** modulo will fit in a **64-bit signed integer**.

A **subarray** is a contiguous part of an array.

 

**Example 1:**
```
Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
```

**Example 2:**
```
Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
```

**Example 3:**
```
Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^7`

# Submissions
---
**Solution 1: (Prefix-sum, centralize over every point)**

**Idea**

* ans = 0
* For each element nums[i] in array nums:
    * We treat nums[i] as minimum number in subarray which includes nums[i]
    * ans = max(ans, nums[i] * getSum(left_bound_index, right_bound_index))
    * left_bound_index: index of the farthest element greater or equal to nums[i] in the left side
    * right_bound_index: index of the farthest element greater or equal to nums[i] in the right side
* How to build left_bound/right_bound array which store index of the farthest element greater or equal to nums[i] in the left side or in the right side?
    * Use stack st which keeps index of elements less than nums[i] so far
    * For i in [0..n-1]:
        * Pop all elements from st which are greater or equal to nums[i]
        * If st is not empty: left_bound[i] = st[-1] + 1 (because st[-1] is index of the nearest element smaller than nums[i])
        * else: left_bound[i] = 0 (because there is no element smaller than nums[i] so far)
        * Add i to st
        
**Complexity**

* Time: `O(N)`
* Space: `O(N)`

```
Runtime: 1560 ms
Memory Usage: 33.2 MB
```
```python
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_bound, right_bound = [0] * n, [0] * n
        st = []
        for i in range(0, n):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                left_bound[i] = st[-1] + 1
            else:
                left_bound[i] = 0
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                right_bound[i] = st[-1] - 1
            else:
                right_bound[i] = n - 1
            st.append(i)

        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        def getSum(left, right):  # left, right inclusive
            return preSum[right + 1] - preSum[left]

        maxProduct = 0
        for i in range(n):
            maxProduct = max(maxProduct, nums[i] * getSum(left_bound[i], right_bound[i]))
        return maxProduct % 1000_000_007
```

**Solution 2: (Mono Stack)**
```
Runtime: 141 ms
Memory: 88.30 MB
```
```c++
class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        long res = 0;
        vector<long> dp(nums.size() + 1), st;
        for (int i = 0; i < nums.size(); ++i)
            dp[i + 1] = dp[i] + nums[i];
        for (int i = 0; i <= nums.size(); ++i) {
            while (!st.empty() && (i == nums.size() || nums[st.back()] > nums[i])) {
                int j = st.back();
                st.pop_back();
                res = max(res, nums[j] * (dp[i] - dp[st.empty() ? 0 : st.back() + 1]));
            }
            st.push_back(i);
        }
        return res % 1000000007;
    }
};
```
