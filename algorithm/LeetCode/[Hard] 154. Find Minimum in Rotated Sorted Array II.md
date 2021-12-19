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
Runtime: 72 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) // 2;           
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
```

**Solution 2: (Binary Search)**

* Time Complexcity O(log N)
* One Thing To Notice If All The Elements Into That Array are going to be Same Then It's Also take O( N ) Time :(

```
Runtime: 16 ms
Memory Usage: 12.4 MB
```
```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0,r = nums.size() - 1,mid = 0;
        while(l < r) {
            mid = l + (r - l) / 2;           
            if (nums[mid] > nums[r]) l = mid + 1;
            else if (nums[mid] < nums[r]) r = mid;
            else r--;
        }
        return nums[l];
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 4 ms
Memory Usage: 6 MB
```
```c


int findMin(int* nums, int numsSize){
    int left = 0, right = numsSize-1, mid;
    while (left < right) {
        mid = left + (right-left)/2;
        if (nums[mid] > nums[right])
            left = mid+1;
        else if (nums[mid] < nums[right])
            right = mid;
        else
            right -= 1;
    }
    return nums[left];
}
```
