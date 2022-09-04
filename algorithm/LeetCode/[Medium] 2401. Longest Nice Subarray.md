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
Runtime: 231 ms
Memory Usage: 57.2 MB
```
```c++
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int used = 0, j = 0, res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            while ((used & nums[i]) != 0)
                used ^= nums[j++];
            used |= nums[i];
            res = max(res, i - j + 1);
        }
        return res;
    }
};
```
