90. Subsets II

Given a collection of integers that might contain duplicates, `nums`, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

# Submissions
---
**Solution:**
```
Runtime: 44 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums and iterate through it
        # For every new element, append that element to every list in result
        # If you see same number, then only append to lists 
        # that you created when you added it in previous iteration
        res = [[]]
        prev = -1
        nums.sort()

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                from_pos = prev
            else:
                from_pos = 0

            prev = len(res)
            for item in res[from_pos:prev]:
                res.append(item + [n])

        return res
```
