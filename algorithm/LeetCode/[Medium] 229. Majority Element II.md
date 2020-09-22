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
**Solution 1: (Boyer-Moore Voting Algorithm)**
```
Runtime: 204 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)
        
        return result
```