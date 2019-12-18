513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

**Example 1:**
```
Input:

    2
   / \
  1   3

Output:
1
```

**Example 2**
```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
```

**Note:** You may assume the tree (i.e., the given root node) is not **NULL**.

# Submissions
---
**Solution 1:**
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        res = None
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            else:
                res = node.val
        return res
```