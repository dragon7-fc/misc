124. Binary Tree Maximum Path Sum

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

**Example 1:**
```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**
```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 84 ms
Memory Usage: 21.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            rst = node.val + max(left, right)
            ans = max(ans, node.val+left+right)
            return max(rst, 0)
        
        dfs(root)
        return ans
```

**Solution 2: (DFS, no global variable)**
```
Runtime: 152 ms
Memory Usage: 21.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        Status = collections.namedtuple('Status', ('max_path_sum', 'max_until_node'))
        
        def helper(node):
            if not node:
                return Status(float('-inf'), 0)
            
            l_status = helper(node.left)
            r_status = helper(node.right)
            
            max_path_sum = max(l_status.max_path_sum, 
                                  r_status.max_path_sum,
                                  node.val + max(l_status.max_until_node, 0) + max(r_status.max_until_node, 0))
            
            max_until_node = max(node.val + max(l_status.max_until_node, 0),  
                                 node.val + max(r_status.max_until_node, 0))
            
            return Status(max_path_sum, max_until_node)
    
        return helper(root).max_path_sum
```