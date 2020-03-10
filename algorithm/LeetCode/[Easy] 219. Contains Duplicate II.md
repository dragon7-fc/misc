219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that **nums[i]** = **nums[j]** and the **absolute** difference between i and j is at most k.

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
```
**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
```
**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 104 ms
Memory Usage: 21.3 MB
```
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        dic = {}
        
        if N == 0:
            return False
        
        dic[nums[0]] = 0
        for i in range(1, N):
            if nums[i] in dic and i-dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i

        return False
```