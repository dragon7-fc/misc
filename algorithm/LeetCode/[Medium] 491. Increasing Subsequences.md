491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

**Example:**
```
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```

**Note:**

* The length of the given array will not exceed `15`.
* The range of integer in the given array is `[-100,100]`.
* The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

# Submissions
---
**Solution 1:**
```
Runtime: 244 ms
Memory Usage: 25.6 MB
```
```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # graph 
        # nodes are index
        # edges are if greater than or eq
        
        # construct
        graph = collections.defaultdict(list)
        for i, v in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[j] >= v:
                    graph[i].append(j)
        
        res = set()
        stack = []
        def dfs(node):
            stack.append(nums[node])
            
            if (len(stack) >= 2):
                seq = tuple(stack)
                res.add(seq)
            
            if node in graph:  # prevent defaultdict adding key on access
                for nei in graph[node]:
                    dfs(nei)
            
            stack.pop()
        
        # dfs each root 
        for root in graph:
            dfs(root)
            
        return [list(seq) for seq in res]
```