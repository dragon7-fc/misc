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
**Solution 1: (DP, Bottom-Up, 1-D)**
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

**Solution 2: (DP, Bottom-Up)**
```
Runtime: 52 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res1 = [0 for i in range(len(nums))]
        res2 = [0 for i in range(len(nums))]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0:
                res1[i] = nums[i]
                res2[i] = nums[i]
            else:
                res1[i] = max(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
                res2[i] = min(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
        
        return max(max(res1), max(res2))
```