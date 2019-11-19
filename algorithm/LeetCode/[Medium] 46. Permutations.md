46. Permutations

Given a collection of **distinct** integers, return all possible permutations.

**Example:**
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return [[]]
        if length == 1: return [[nums[0]]]
        res=[]
        for i in range(length):
            r = self.permute(nums[:i] + nums[i+1:]) 
            res += [[nums[i]]+x for x in r]
            
        return res
```