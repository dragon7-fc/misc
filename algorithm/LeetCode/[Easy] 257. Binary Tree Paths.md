257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

**Example:**
```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

# Submissions
---
**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(node, path):
            nonlocal ans
            if not node.left and not node.right:
                ans.append(path)
                return
            if node.left:
                dfs(node.left, '{}->{}'.format(path, node.left.val))
            if node.right:
                dfs(node.right, '{}->{}'.format(path, node.right.val))
            
        if not root:
            return ""
        dfs(root, str(root.val))
        return ans
```