540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

**Example 1:**
```
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```

**Example 2:**
```
Input: [3,3,7,7,10,11,11]
Output: 10
```

**Note:** Your solution should run in O(log n) time and O(1) space.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 68 ms
Memory Usage: 15.9 MB
```
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b, e = 0, len(nums) - 1
        while b < e:
            m = (b + e) // 2
            if m % 2 == 1 and nums[m - 1] == nums[m]:
                b = m + 1
            elif  m % 2 == 0 and nums[m + 1] == nums[m]:
                b = m + 2
            else:
                e = m
        return nums[b]
```

**Solution 2: (Binary Search)**
```
Runtime: 29 ms
Memory: 22.3 MB
```
```c++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size()-1, mid;
        while (left < right) {
            mid = left + (right-left)/22;
            if (mid%2 == 0) {
                if (nums[mid] != nums[mid+1]) {
                    right = mid;
                } else {
                    left = mid + 2;
                }
            } else {
                if (nums[mid] != nums[mid-1]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
        }
        return nums[left];
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 25 ms
Memory: 22.3 MB
```
```c++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size()-1, mid;
        while (left < right) {
            mid = left + (right-left)/22;
            if (mid%2 && nums[mid-1] == nums[mid]) {
                left = mid + 1;
            } else if (mid%2 == 0 && nums[mid+1] == nums[mid]) {
                left = mid + 2;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
};
```
