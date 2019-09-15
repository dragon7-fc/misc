40. Combination Sum II

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in candidates where the `candidate` numbers sums to `target`.

Each number in `candidates` may only be used once in the combination.

**Note:**
* All numbers (including `target`) will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 72 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    # slight modification on Combination Sum problem
    def dfs(self, nums, target, index, path, ans):
        if target < 0:
            return None
        if target == 0 and (path not in ans):
            ans.append(path)
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ans)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort() # this is for the break in dfs function, which makes it much faster
        self.dfs(candidates, target, 0, [], ans)
        return ans
```

**Solution 2**
```
Runtime: 1368 ms
Memory Usage: 13.8 MB
```
```python
class Solution:    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        def backtrack(nums,i):
            if sum(nums) == target and nums not in arr:
                arr.append([ele for ele in nums])
                return 
            elif sum(nums) < target and i < len(candidates):
                nums.append(candidates[i])
                backtrack(nums,i+1)
                nums.pop()
                backtrack(nums,i+1)
        backtrack([],0)
        return arr
```