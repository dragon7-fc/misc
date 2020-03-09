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
**Solution 1: (DP)**
```
Runtime: 60 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_so_far = min_so_far = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(ans, max_so_far)
        
        return ans           
```