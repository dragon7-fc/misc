154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:**
```
Input: [1,3,5]
Output: 1
```

**Example 2:**
```
Input: [2,2,2,0,1]
Output: 0
```

**Note:**

* This is a follow up problem to Find Minimum in Rotated Sorted Array.
* Would allow duplicates affect the run-time complexity? How and why?

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 48 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums)-1
        # [5,6,7,7,0,1,2]
        while lo <= hi:
            # push left forward until no duplicate
            while lo+1 < len(nums) and nums[lo] == nums[lo+1]:
                lo += 1 
            while hi-1 >= 0 and nums[hi] == nums[hi-1]:
                hi -= 1

            # push right backword until no duplicate 
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            elif nums[mid] < nums[hi]:
                # skip the duplicate 
                while mid-1 >= 0 and nums[mid-1] == nums[mid]:
                    mid -= 1
                if mid-1 < 0 or nums[mid] <= nums[mid-1]:
                    return nums[mid]
                else:
                    hi = mid-1 
            else:
                return nums[mid]
```