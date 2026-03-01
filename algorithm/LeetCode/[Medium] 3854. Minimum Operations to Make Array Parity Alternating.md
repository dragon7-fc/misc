3854. Minimum Operations to Make Array Parity Alternating

You are given an integer array `nums`.

An array is called **parity alternating** if for every index `i` where `0 <= i < n - 1`, `nums[i]` and `nums[i + 1]` have different parity (one is even and the other is odd).

In one operation, you may choose any index `i` and either increase `nums[i]` by 1 or decrease `nums[i]` by 1.

Return an integer array `answer` of length 2 where:

`answer[0]` is the **minimum** number of operations required to make the array parity alternating.
`answer[1]` is the **minimum** possible value of `max(nums) - min(nums)` taken over all arrays that are parity alternating and can be obtained by performing exactly answer[0] operations.

An array of length 1 is considered parity alternating.

 

**Example 1:**
```
Input: nums = [-2,-3,1,4]

Output: [2,6]

Explanation:

Applying the following operations:

Increase nums[2] by 1, resulting in nums = [-2, -3, 2, 4].
Decrease nums[3] by 1, resulting in nums = [-2, -3, 2, 3].
The resulting array is parity alternating, and the value of max(nums) - min(nums) = 3 - (-3) = 6 is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.
```

**Example 2:**
```
Input: nums = [0,2,-2]

Output: [1,3]

Explanation:

Applying the following operation:

Decrease nums[1] by 1, resulting in nums = [0, 1, -2].
The resulting array is parity alternating, and the value of max(nums) - min(nums) = 1 - (-2) = 3 is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.
```

**Example 3:**
```
Input: nums = [7]

Output: [0,0]

Explanation:

No operations are required. The array is already parity alternating, and the value of max(nums) - min(nums) = 7 - 7 = 0, which is the minimum possible.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-109 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 28 ms, Beats 90.00%
Memory: 243.22 MB, Beats 30.00%
```
```c++
class Solution {
public:
    vector<int> makeParityAlternating(vector<int>& nums) {
        int n = nums.size(), i;
        if (n == 1) {
            return {0, 0};
        }
        int k[2] = {0}, mx[2] = {INT_MIN, INT_MIN}, mn[2] = {INT_MAX, INT_MAX};
        for (i = 0; i < n; i ++) {
            if (i % 2 == ((nums[i] % 2) + 2) % 2) {
                mx[0] = max(mx[0], nums[i]);
                mn[0] = min(mn[0], nums[i]);
            } else {
                k[0] += 1;
            }
        }
        if (k[0]) {
            for (i = 0; i < n; i ++) {
                if (i % 2 != ((nums[i] % 2) + 2) % 2) {
                    if (nums[i] > mx[0]) {
                        mx[0] = max(mx[0], nums[i] - 1);
                    } else if (nums[i] < mn[0]) {
                        mn[0] = min(mn[0], nums[i] + 1);
                    }
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (i % 2 != ((nums[i] % 2) + 2) % 2) {
                mx[1] = max(mx[1], nums[i]);
                mn[1] = min(mn[1], nums[i]);
            } else {
                k[1] += 1;
            }
        }
        if (k[1]) {
            for (i = 0; i < n; i ++) {
                if (i % 2 == ((nums[i] % 2) + 2) % 2) {
                    if (nums[i] > mx[1]) {
                        mx[1] = max(mx[1], nums[i] - 1);
                    } else if (nums[i] < mn[1]) {
                        mn[1] = min(mn[1], nums[i] + 1);
                    }
                }
            }
        }
        if (k[0] < k[1]) {
            return {k[0], mx[0] == mn[0] ? 1 : mx[0] - mn[0]};
        } else if (k[0] > k[1]) {
            return {k[1], mx[1] == mn[1] ? 1: mx[1] - mn[1]};
        } else {
            if (mx[0] == mn[0] || mx[1] == mn[1]) {
                return {k[0], 1};
            }
            return {k[0], min(mx[0] - mn[0], mx[1] - mn[1])};
        }
    }
};
```
