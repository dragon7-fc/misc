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
**Solution 1: (DFS)**
```
Runtime: 44 ms
Memory Usage: 15 MB
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
        self.depth = float('Inf')
        def dfs(node, depth):
            if not node:return
            if not node.right and not node.left:
                self.depth = min(self.depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        if not root:return 0
        dfs(root, 1)
        return self.depth
```

**Solution 2: (BFS)**
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