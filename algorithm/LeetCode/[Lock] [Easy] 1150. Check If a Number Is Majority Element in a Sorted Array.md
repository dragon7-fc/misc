1150. Check If a Number Is Majority Element in a Sorted Array

Given an array `nums` sorted in **non-decreasing** order, and a number `target`, return `True` if and only if `target` is a majority element.

A majority element is an element that appears **more than** `N/2` times in an array of length `N`.

 

**Example 1:**
```
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
```

**Example 2:**
```
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: 
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^9`
* `1 <= target <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 36 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        def binary_search(nums, num):
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = int(l/2 + r/2)
                if nums[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            if l == len(nums) - 1 and nums[l] != num:
                return l + 1
            return l
        
        
        left = binary_search(nums, target)
        right = binary_search(nums, target + 1) - 1
        
        return (right - left + 1) > len(nums) / 2
```

**Solution 2: (Binary Search)**
```
Runtime: 4 ms
Memory Usage: 7.7 MB
```
```c++
class Solution {
public:
    std::size_t lower_bound(const std::vector<int>& nums, std::size_t first, std::size_t last, std::int64_t target)
    {
        while (first < last)
        {
          std::size_t pivot = first + (last - first) / 2;
          if (nums[pivot] < target)
            first = pivot + 1;
          else
            last = pivot;
        }
        return first;
    }
    bool isMajorityElement(vector<int>& nums, int target) {
        std::ios::sync_with_stdio(false);
        auto idx1 = lower_bound(nums, 0, nums.size(), target);
        if (idx1 == nums.size())
          return false;

        auto idx2 = lower_bound(nums, idx1 + 1, nums.size(), static_cast<std::int64_t>(target) + 1);
        auto n = idx2 - idx1;
        return n > nums.size() / 2;
    }
};
```