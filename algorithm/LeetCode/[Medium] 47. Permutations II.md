47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 336 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def backtrack(nums, permutation):
            if len(permutation) == N:
                ans.add(tuple(permutation))
                return
            for i in range(len(nums)):
                permutation.append(nums[i])
                backtrack(nums[:i]+nums[i+1:], permutation)
                permutation.pop()
        ans = set()
        permutation = []
        backtrack(nums, permutation)
        
        return ans
```