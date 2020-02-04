216. Combination Sum III

Find all possible combinations of **k** numbers that add up to a number **n**, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**
* All numbers will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: k = 3, n = 7
Output: [[1,2,4]]
```
**Example 2:**
```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```
# Submissions
---
**Solution1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(index, target, path):
            if target < 0 or len(path) > k:
                return None
            if target == 0 and (len(path) == k) and (path not in ans):
                ans.append(path)
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break
                backtrack(i+1, target-nums[i], path+[nums[i]])
        ans = []
        nums = [i for i in range(1, 10)]
        backtrack(0, n, [])
        
        return ans
```