3583. Count Special Triplets

You are given an integer array `nums`.

A **special triplet** is defined as a triplet of indices `(i, j, k)` such that:

* `0 <= i < j < k < n`, where `n = nums.length`
* `nums[i] == nums[j] * 2`
* `nums[k] == nums[j] * 2`

Return the total number of **special triplets** in the array.

Since the answer may be large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
```

**Example 2:**
```
Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0
```

**Example 3:**
```
Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

(i, j, k) = (0, 1, 3)
nums[0] = 8, nums[1] = 4, nums[3] = 8
nums[0] = nums[1] * 2 = 4 * 2 = 8
nums[3] = nums[1] * 2 = 4 * 2 = 8
(i, j, k) = (1, 2, 4)
nums[1] = 4, nums[2] = 2, nums[4] = 4
nums[1] = nums[2] * 2 = 2 * 2 = 4
nums[4] = nums[2] * 2 = 2 * 2 = 4
```

**Constraints:**

* `3 <= n == nums.length <= 10^5`
* `0 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Prefix Sum, Counter, left and right)**
```
Runtime: 54 ms, Beats 81.82%
Memory: 198.80 MB, Beats 81.82%
```
```c++
class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        int n = nums.size(), i, MOD = 1e9+7;
        long long right[100001] = {0}, left[100001] = {0}, ans = 0;
        for (i = n-1; i >= 0; i --) {
            right[nums[i]] += 1;
        }
        for (i = 0; i < n-1; i ++) {
            right[nums[i]] -= 1;
            if (nums[i]*2 <= 100000) {
                ans += left[nums[i]*2] * right[nums[i]*2];
            }
            ans %= MOD;
            left[nums[i]] += 1;
        }
        return ans;
    }
};
```
