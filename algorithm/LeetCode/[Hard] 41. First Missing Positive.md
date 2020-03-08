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
**Solution 1: (Sort)**

Just like swap and place the number to the correct index place.  
After placing them to the correct place, go through the array again to check if the number is right, if not then we have the missing index.
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] <= 0 or nums[i] > N:
                i += 1
                continue
            j = nums[i]
            if nums[j-1] != nums[i]:
                nums[j-1], nums[i] = nums[i], nums[j-1]
            else:
                i += 1
        
        for i in range(N):
            if i + 1 != nums[i]:
                return i + 1
        return N + 1
```

**Solution 2: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while i in nums:
            i = i+1
        return i
```