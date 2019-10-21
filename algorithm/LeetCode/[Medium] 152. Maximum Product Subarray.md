152. Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

# Submissions
---
**Solution 1:**
```
Runtime: 52 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = local_min = global_max = nums[0] # initial all to first num
        for num in nums[1:]:
            local_min, _, local_max = sorted([local_max * num, local_min * num, num]) # sort will take care of all the if
            if local_max > global_max:
                global_max = local_max
        return global_max               
```