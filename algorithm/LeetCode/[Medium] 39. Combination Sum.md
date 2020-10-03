39. Combination Sum

Given a set of candidate numbers (`candidates`) (without duplicates) and a target number (`target`), find all unique combinations in candidates where the `candidate` numbers sums to `target`.

The same repeated number may be chosen from `candidates` unlimited number of times.

**Note:**
* All numbers (including `target`) will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**
```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 92 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []
        candidates.sort()
        
        def dfs(total, index, path, res):
            if total < 0:
                return
            if total == 0:
                res.append(path)
                return
            for i in range(index, N):
                dfs(total-candidates[i], i, path+[candidates[i]], res)

        dfs(target, 0, [], res)
        return res
```

**Solution 2: (Backtrack)**
```
Runtime: 188 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        def backtrack(nums,i):
            if sum(nums) == target:
                arr.append([ele for ele in nums])
                return 
            elif sum(nums) < target and i < len(candidates):
                nums.append(candidates[i])
                backtrack(nums,i)
                nums.pop()
                backtrack(nums,i+1)
        backtrack([],0)
        return arr
```

**Solution 3: (DP)**
```
Runtime: 132 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[[] for _ in range(len(candidates))] for _ in range(target+1)]
        for n in range(1, target+1):
            for i, a in enumerate(candidates):
                if n == a:
                    dp[n][i].append([a])
                else:
                    if n - a < 0: continue
                    for b in dp[n-a][i:]:
                        for s in b:
                            dp[n][i].append([a, *s])
                            
        return [s for b in dp[-1] for s in b]
```