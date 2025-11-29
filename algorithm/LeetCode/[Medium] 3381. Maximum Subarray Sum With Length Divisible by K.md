3381. Maximum Subarray Sum With Length Divisible by K

You are given an array of integers `nums` and an integer `k`.

Return the **maximum** sum of a non-empty **subarray** of `nums`, such that the size of the subarray is **divisible** by `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.
```

**Example 2:**
```
Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.
```

**Example 3:**
```
Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.
```
 

**Constraints:**

* `1 <= k <= nums.length <= 2 * 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Hash Table, Prefix Sum)**

       9  -11   15
a   0  9   -2   13
pre
0          -2
1      9  
ans        -2    4

```
Runtime: 4 ms, Beats 91.47%
Memory: 162.30 MB, Beats 90.10%
```
```c++
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size(), i;
        long long a = 0, ans = LONG_LONG_MIN;
        vector<long long> pre(k);
        for (i = 0; i < n; i ++) {
            a += nums[i];
            if (i >= k - 1) {
                ans = max(ans, a - pre[(i + 1) % k]);
                pre[(i + 1) % k] = min(pre[(i + 1) % k], a);
            } else {
                pre[(i + 1) % k] = a;
            }
        }
        return ans;
    }
};
```
