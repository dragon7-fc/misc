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

**Solution 4: (Binary Search)**
```
Runtime: 3 ms
Memory Usage: 11.1 MB
```
```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0 , right = nums.size() -1, mid;
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
};
```

**Solution 5: (Binary Search)**
```
Runtime: 80 ms
Memory: 14.3 MB
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:   
                # left part sorted
                if nums[left] <= target < nums[mid]:  # target in sorted left part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right part sort
                if nums[mid] < target <= nums[right]:  # target in sorted right part
                    left = mid+1
                else:
                    right = mid-1
        return -1
```

**Solution 6: (Binary Search)**

case1:
         /
      /   
   /  
           /
   ^l   ^m  ^r  

case2:
   /     
          / 
        / 
     /
   ^l  ^m  ^r

                        v
    4,   5,   6,   7,   0,   1,   2
    ^l             ^m             ^r
                        ^l   ^m    ^r
                        ^lrm
    
                
    [4,   5,   6,   7,   0,   1,   2],    target = 3
     ^l             ^m             ^r
                        ^l    ^m   ^r
                                   ^lrm

            v
        3   1,      target = 1
        ^lm ^r


```
Runtime: 0 ms, Beats 100.00%
Memory: 15.25 MB, Beats 32.89%
```
```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size(), left = 0, right = n - 1, mid;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[left] <= nums[mid]) {
                                // ^ 2 element
                if (nums[left] <= target && target <= nums[mid]) {
                             // ^ 2 element
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};
```
