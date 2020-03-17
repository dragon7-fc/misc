95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique **BST**'s (binary search trees) that store values 1 ... n.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Submissions:
---
**Solution 1: (DP Top-Down)**
```
Runtime: 56 ms
Memory Usage: 13.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        @functools.lru_cache(None)
        def dfs(l, r):   # split between [l, r)
            if l == r:
                return [None]  # list contain None object
            rst = []
            for i in range(l, r):
                for lchild in dfs(l, i):
                    for rchild in dfs(i+1, r):
                        root = TreeNode(i+1)   # +1 to convert the index to the actual value
                        root.left = lchild
                        root.right = rchild
                        rst.append(root)
            return rst
        
        return dfs(0, n) if n else []
```