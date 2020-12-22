110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

**Example 1:**
```
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
```

**Example 2:**
```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 52 ms
Memory Usage: 17.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True
        
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            if self.isBalanced:
                self.isBalanced = abs(left - right) < 2 
            
            return 1 + max(left, right)
    
    
        height(root)
        return self.isBalanced
```