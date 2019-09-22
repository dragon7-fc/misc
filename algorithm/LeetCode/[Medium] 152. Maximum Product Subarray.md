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
Runtime: 64 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = overall_max = nums[0]
        
        for num in nums[1:]:
            temp_max = max(num, min_*num, max_*num)
            min_ = min(num, min_*num, max_*num)
            max_ = temp_max
            overall_max =  max(overall_max, max_)
            
        return overall_max                   
```