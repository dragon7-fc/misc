33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of $O(log n)$.

**Example 1:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

# Submissions
---
**Solution 1: (recursive)**
```
196 / 196 test cases passed.
Status: Accepted
Runtime: 52 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right, target):
            if left > right:
                return -1
            
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid            
            elif nums[left] <= target < nums[mid] \
                or nums[mid] < nums[left] and target < nums[mid] \
                or nums[mid] < nums[left] and target >= nums[left]:
                return binary_search(left, mid-1, target)
            else:
                return binary_search(mid+1, right, target)        
            
        return binary_search(0, len(nums)-1, target)
```

**Solution 2: (iterative)**
```
Runtime: 52 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        ans = -1
        
        while left <= right:
            mid = (left+right) // 2

            if target == nums[mid]:
                ans = mid
                break
            elif nums[left] <= target < nums[mid] \
                or nums[mid] < nums[left] and target < nums[mid] \
                or nums[mid] < nums[left] and target >= nums[left]:
                right = mid-1
            else:
                left = mid+1

        return ans
```

**Solution 3:**
```
Runtime: 48 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                if nums[m] >= nums[l] or target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] <= nums[r] or target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
```