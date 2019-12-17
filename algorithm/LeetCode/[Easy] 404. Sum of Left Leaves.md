404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

**Example:**
```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```

**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 13.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, is_left):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                if is_left:
                    ans += node.val
                return
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return ans
```