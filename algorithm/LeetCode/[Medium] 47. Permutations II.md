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

**Solution 2: (itertools)**
```
Runtime: 84 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a = {tuple(x) for x in itertools.permutations(nums)}
        res = []
        for x in a: res.append(list(x))
        return res
```

**Solution 3: (DFS)**
```
Runtime: 56 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def shouldSwap(start,curr,nums):
            for i in range(start,curr):
                if nums[i]==nums[curr]:
                    return False
            return True
        
        def dfs(nums,path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if shouldSwap(0,i,nums):
                    dfs(nums[:i]+nums[i+1:],path+[nums[i]])

        dfs(nums,[])
        return res
```