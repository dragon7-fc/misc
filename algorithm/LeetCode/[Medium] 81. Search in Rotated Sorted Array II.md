81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return true, otherwise return false.

**Example 1:**
```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**
```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Follow up:**

* This is a follow up problem to Search in Rotated Sorted Array, where `nums` may contain duplicates.
* Would this affect the run-time complexity? How and why?

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 60 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in set(nums): return True
```

**Solution 2: (DFS, Binary Search)**
```
Runtime: 52 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False

        def dfs(left, right):
            if left >= right: return False
            mid = left + (right - left) // 2
            if nums[mid] == target: return True
            if nums[mid] == nums[left] and nums[left] == nums[right - 1]:
                return dfs(left, mid) or dfs(mid + 1, right)
            if nums[mid] >= nums[left]:                
                return dfs(left, mid) if nums[left] <= target < nums[mid] else dfs(mid + 1, right)
            else:
                return dfs(mid + 1, right) if nums[mid] < target <= nums[right - 1] else dfs(left, mid)
        
        return dfs(0, len(nums))
```