530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

**Example:**
```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```

**Note:** There are at least two nodes in this BST.

# Submissions
---
**Solution 1:**
```
Runtime: 56 ms
Memory Usage: 14.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        v = []
        def dfs(node):
            nonlocal v
            if not node:
                return
            dfs(node.left)
            v += [node.val]
            dfs(node.right)
            
        dfs(root)
        return min([v[i] - v[i-1] for i in range(1, len(v))])
```