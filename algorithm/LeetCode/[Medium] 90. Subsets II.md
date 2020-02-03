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
**Solution 1:**
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
**Solution 2: (Recursion)**
```
Runtime: 36 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return set(tuple(el) for el in output)
```

**Solution3: (itertools)**
```
Runtime: 32 ms
Memory Usage: 12.5 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        m = [[i for i in itertools.combinations(nums,j)] for j in range(len(nums)+1)]
        m1 = [tuple(sorted(i)) for j in m for i in j]
        return list(set(m1))
```

**Solution 4: (DFS, Backtracking)**
```
Runtime: 36 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(choice, temp_res):
            res.append(temp_res)
            seen = set()
            if len(temp_res) == len(nums):
                return
            for i, n in enumerate(choice):
                if n not in seen:
                    seen.add(n)
                    backtrack(choice[i+1:], temp_res + [n])    
        backtrack(sorted(nums), [])
        
        return res
```