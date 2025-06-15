3584. Maximum Product of First and Last Elements of a Subsequence

You are given an integer array `nums` and an integer `m`.

Return the **maximum** product of the first and last elements of any subsequence of `nums` of size `m`.

 

**Example 1:**
```
Input: nums = [-1,-9,2,3,-2,-3,1], m = 1

Output: 81

Explanation:

The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.
```

**Example 2:**
```
Input: nums = [1,3,-5,5,6,-4], m = 3

Output: 20

Explanation:

The subsequence [-5, 6, -4] has the largest product of the first and last elements.
```

**Example 3:**
```
Input: nums = [2,-1,2,-6,5,2,-5,7], m = 2

Output: 35

Explanation:

The subsequence [5, 7] has the largest product of the first and last elements.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-105 <= nums[i] <= 10^5`
* `1 <= m <= nums.length`

# Submissions
---
**Solution 1: (Sliding Window, DP Bottom-Up)**
```
Runtime: 9 ms, Beats 50.00%
Memory: 175.37 MB,  Beats -%
```
```c++
class Solution {
public:
    long long maximumProduct(vector<int>& nums, int m) {
        long long ma = nums[0], mi = nums[0], ans = 1LL * nums[0] * nums[m - 1];
        for (int i = m - 1; i < nums.size(); ++i) {
            ma = max(ma, (long long)nums[i - m + 1]);
            mi = min(mi, (long long)nums[i - m + 1]);
            ans = max({ans, mi * nums[i], ma * nums[i]});
        }
        return ans;
    }
};
```
