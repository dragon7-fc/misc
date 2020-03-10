229. Majority Element II

Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

**Note:** The algorithm should run in linear time and in $O(1)$ space.

**Example 1:**
```
Input: [3,2,3]
Output: [3]
```
**Example 2:**
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

# Submissions
---
**Solution 1: (Vote)**
```
Runtime: 144 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        res1 = 0
        res2 = 0
        size = len(nums)
        for num in nums:
            if res1 == num:
                count1 += 1
            elif res2 == num:
                count2 += 1
            elif count1 == 0:
                res1 = num
                count1 = 1
            elif count2 == 0:
                res2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if res1 == num:
                count1 += 1
            elif res2 == num:
                count2 += 1
        res = []
        if count1 > size/3:
            res.append(res1)
        if count2 > size/3:
            res.append(res2)
        return res
```
