111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its minimum depth = 2.

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 14.5 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            return 1 + min(left_depth, right_depth) if (left_depth > 0 and right_depth > 0) else 1 + max(left_depth,right_depth)
        return 0
```

**Solution 2:**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = collections.deque()
        q.append((root,1))
        
        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
                return level
            
            for node in [node.left, node.right]:
                if node:
                    q.append((node, level+1))
```