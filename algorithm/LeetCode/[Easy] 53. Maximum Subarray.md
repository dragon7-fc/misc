53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**
```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
```

**Follow up:**

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Submissions
---
**Solution 1:**
```
Runtime: 60 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
```

**Solution 2:**
```
Runtime: 48 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_sum = 0
        tmp_sum = 0
        for i in range(len(nums)):
            tmp_sum = tmp_sum + nums[i]
            if tmp_sum >= max_sum:
                max_sum = tmp_sum
            if tmp_sum < 0:
                tmp_sum = 0
        
        if max_sum == 0:
            return max(nums)
        return max_sum        
```

**Solution 3:**
```
Runtime: 84 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur = float('-inf')
        for x in nums:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        return ans
```