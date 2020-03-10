228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

**Example 1:**
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```
**Example 2:**
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        N = len(nums)
        i, j = 0, 0
        ans = []
        while i < N:
            while j + 1 < N and nums[j + 1] == nums[j] + 1:
                j += 1
            if i != j:
                ans.append('{}->{}'.format(nums[i], nums[j]))
            else:
                ans .append('{}'.format(str(nums[i])))
            j = j + 1
            i = j
            
        
        return ans
```
