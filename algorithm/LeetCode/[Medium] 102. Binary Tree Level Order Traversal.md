102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```

# Submissions
---
**Solution 1: (Level-Order)**
```
Runtime: 32 ms
Memory Usage: 14.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root] if root else None
        ans = []
        while q:
            nq = []
            cur = []
            for node in q:
                cur += [node.val]
                for c in [node.left, node.right]:
                    if c:
                        nq += [c]
            ans += [cur]
            q = nq
        return ans
        
```