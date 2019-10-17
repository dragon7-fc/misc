41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

**Example 1:**
```
Input: [1,2,0]
Output: 3
```

**Example 2:**
```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:**
```
Input: [7,8,9,11,12]
Output: 1
```
**Note:**

* Your algorithm should run in O(n) time and uses constant extra space.

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                # item is at proper position.
                i += 1
            elif len(nums) + 1 <= nums[i] or nums[i] <= 0:
                i += 1
            else:
                # We want to put nums in the right position.
                next_i = nums[i] - 1
                nums[i] = nums[next_i] # haven't found the right one for this yet.
                nums[next_i] = next_i + 1

                if nums[next_i] == nums[i]:
                    i += 1

        for e, i in enumerate(nums):
            if i != e + 1:
                return e + 1
        return len(nums) + 1
```