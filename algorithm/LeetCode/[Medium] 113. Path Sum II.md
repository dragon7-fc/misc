113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 17.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        def dfs(node, path_sum, path):
            nonlocal ans
            if not node:
                return False
            if node.val == path_sum and not node.left and not node.right:
                ans += [path]
                return
            else:
                if node.left:
                    dfs(node.left, path_sum-node.val, path + [node.left.val])
                if node.right:
                    dfs(node.right, path_sum-node.val, path + [node.right.val])
            return
        
        dfs(root, sum, [root.val])
        return ans
```