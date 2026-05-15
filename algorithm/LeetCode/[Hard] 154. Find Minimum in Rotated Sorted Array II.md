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

**Solution 4: (Bionary Search)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.22 MB, Beats 28.32%
```
```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, mid, ans = INT_MAX;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (right - left >= 2 && nums[mid] == nums[left] && nums[mid] == nums[right]) {
                left += 1;
                right -= 1;
            } else if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                ans = min(ans, nums[mid]);
                right = mid - 1;
            }
        }
        return ans;
    }
};
```

**Solution 5: (Binary Search, transfer to unique element case)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.14 MB, Beats 63.69%
```
```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size(), left = 0, right = n - 1, mid;
        while (left < right) {

            // remove duplicate
            if (nums[left] == nums[mid]) {
                left = mid;
            }
            while (mid < right && nums[right] == nums[mid]) {
                right -= 1;
            }

            mid = left + (right - left) / 2;
            if (nums[right] < nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
};
```

**Solution 5: (Binary Search, if left and right not match then left mid right should have duplicate)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.04 MB, Beats 90.00%
````
```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size(), left = 0, right = n - 1, mid;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (nums[right] < nums[mid]) {
                left = mid + 1;
            } else if (nums[left] < nums[mid]) {
                right = mid;
            } else {
                // duplicate
                right -= 1;
            }
        }
        return nums[left];
    }
};
```
