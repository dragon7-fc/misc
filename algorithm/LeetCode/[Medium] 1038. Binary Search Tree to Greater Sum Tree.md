1038. Binary Search Tree to Greater Sum Tree

Given the root of a **binary search tree** with distinct values, modify it so that every `node` has a new value equal to the sum of the values of the original tree that are greater than or equal to `node.val`.

As a reminder, a binary search tree is a tree that satisfies these constraints:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.
 

**Example 1:**

![1038_tree.png](img/1038_tree.png)
```
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

**Constraints:**

* The number of nodes in the tree is between `1` and `100`.
* Each node will have value between `0` and `100`.
* The given tree is a binary search tree.
* Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

# Submissions
---
**Solution 1: (Binary Search Tree, Recursive)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    total = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.bstToGst(root.right)
            self.total += root.val
            root.val = self.total
            self.bstToGst(root.left)
        return root
```

**Solution 2: (Binary Search Tree, Iterative)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root
```