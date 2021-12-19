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
Runtime: 44 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right, target):
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid            
            elif (nums[left] <= target < nums[mid] or
                    target <= nums[mid] < nums[left] or
                    nums[mid] < nums[left] <= target):
                return binary_search(left, mid-1, target)
            else:
                return binary_search(mid+1, right, target)        
            
        return binary_search(0, len(nums)-1, target)
            
```

**Solution 2: (iterative)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                ans = mid
                break
            elif (nums[left] <= target < nums[mid] or
                    target <= nums[mid] < nums[left] or
                    nums[mid] < nums[left] <= target):
                right = mid - 1
            else:
                left = mid + 1

        return ans 
```

**Solution 3: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c
int search(int* nums, int numsSize, int target){
    int left = 0 , right = numsSize -1, mid;
    while (left <= right) {
        mid = (left + right) / 2;
        if (nums[mid] == target)
            return mid;
        else if (nums[left] <= target && target < nums[mid] 
                || target < nums[mid] && nums[mid] < nums[left] 
                || nums[mid] < nums[left] && nums[left] <= target)
            right = mid - 1;
        else
            left = mid + 1;
    }
    return -1;
}
```
