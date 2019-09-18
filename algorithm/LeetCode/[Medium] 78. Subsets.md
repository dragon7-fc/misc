78. Subsets

Given a set of **distinct** integers, nums, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: N/A
```
```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(nums==[]):
            return [[]]
        allSubsets = []
        for subset in self.subsets(nums[1:]):
            allSubsets += [subset]
            allSubsets += [[nums[0]]+subset]
        return allSubsets
```

**Solution 2:**
```
Runtime: 40 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res += [s + [n] for s in res]
        return res
```
```
nums = [1,2,3]
Initialize the array to be returned as [[]]

i       nums[i]     res = res + [s + [nums[i]] for s in res]
0       1           [[]] + [[]+[1]] = [[], [1]]
1       2           [[], [1]] + [[]+[2]] + [[1]+[2]] = [[], [1], [2], [1, 2]]
2       3           [[], [1], [2], [1, 2]] + [[]+[3]] + [[1]+[3]] + [[2]+[3]] + [[1,2]+[3]] = [[], [1], [2], [1,2], [3], [1, 3], [2, 3], [1, 2, 3]]
```