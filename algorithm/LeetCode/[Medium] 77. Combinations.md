77. Combinations

Given two integers `n` and `k`, return all possible combinations of `k` numbers out of `1 ... n`.

**Example:**
```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 112 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(nums, combination):
            if len(nums) < k - len(combination):
                return
            if len(combination) == k:
                ans.append(combination)
            else:
                for i, num in enumerate(nums):
                    backtrack(nums[i+1:], combination + [num])
        backtrack([_ for _ in range(1, n+1)], [])
            
        return ans
```

**Solution 2: (itertools)**
```
Runtime: 72 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1,n+1)]
        return [_ for _ in itertools.combinations(nums, k)]
```