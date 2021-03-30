325. Maximum Size Subarray Sum Equals k

Given an integer array `nums` and an integer `k`, return the maximum length of a subarray that sums to `k`. If there isn't one, return `0` instead.

 

**Example 1:**
```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:**
```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

**Constraints:**

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `-10^5 <= k <= 10^5`
 

Follow Up: Can you do it in `O(n)` time?

# Submissions
---
**SOlution 1: (Prefix Sum)**
```
Runtime: 112 ms
Memory Usage: 17.2 MB
```
```python
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums = {0: -1}  # key=current sum, val = index
        max_len = 0
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            target = current_sum - k
            if target in sums:
                max_len = max(max_len, i-sums[target])
            if current_sum not in sums:
                sums[current_sum] = i
        return max_len
```