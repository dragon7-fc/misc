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
**Solution 1: (Backtracking)**
```
Runtime: 28 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results
```