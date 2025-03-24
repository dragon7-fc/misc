2401. Longest Nice Subarray

You are given an array `nums` consisting of positive integers.

We call a subarray of `nums` **nice** if the bitwise **AND** of every pair of elements that are in **different** positions in the subarray is equal to `0`.

Return the length of the **longest** nice subarray.

A **subarray** is a **contiguous** part of an array.

**Note** that subarrays of length `1` are always considered nice.

 

**Example 1:**
```
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
```

**Example 2:**
```
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 1051 ms
Memory Usage: 28.8 MB
```
```python
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = AND = i = 0
        for j in range(len(nums)):
            while AND & nums[j]:
                AND ^= nums[i]
                i += 1
            AND |= nums[j]
            res = max(res, j - i + 1)
        return res
```

**Solution 2: (Sliding Window)**
```
Runtime: 140 ms, Beats 10.96%
Memory: 60.94 MB, Beats 64.15%
```
```c++
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size(), i = 0, j, k, ck = 0, cnt[32] = {0}, cur = 0, ans = 1;
        for (j = 0; j < n; j ++) {
            k = 0;
            while ((1<<k) <= nums[j]) {
                if ((1<<k) & nums[j]) {
                    cnt[k] += 1;
                    if (cnt[k] == 2) {
                        ck += 1;
                    }
                }
                k += 1;
            }
            while (ck) {
                k = 0;
                while ((1<<k) <= nums[i]) {
                    if ((1<<k) & nums[i]) {
                        cnt[k] -= 1;
                        if (cnt[k] == 1) {
                            ck -= 1;
                        }
                    }
                    k += 1;
                }
                i += 1;
            }
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
```

**Solution 3: (Sliding Window, optimizzed)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 61.05 MB, Beats 28.44%
```
```c++
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size(), i = 0, j, pre = 0, ans = 0;
        for (j = 0; j < n; j ++) {
            while ((pre & nums[j]) != 0) {
                pre ^= nums[i];
                i += 1;
            }
            pre ^= nums[j];
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
```
