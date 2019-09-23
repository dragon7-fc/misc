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
**Solution**
```
Runtime: 28 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        nums.append(-1)
        N = len(nums)
        start = end = 0
        ans = []
        for i in range(1, N):
            if i <= N-1 and nums[i] != nums[i-1]+1:
                end = i-1     
                if start != end:
                    ans.append("{}->{}".format(nums[start], nums[end]))
                else:
                    ans.append("{}".format(nums[start]))
                start = i
            
        return ans
```
