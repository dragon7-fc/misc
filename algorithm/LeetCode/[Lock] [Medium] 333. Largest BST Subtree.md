333. Largest BST Subtree

Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A **Binary Search Tree (BST)** is a tree in which all the nodes follow the below-mentioned properties:

* The left subtree values are less than the value of their parent (root) node's value.
* The right subtree values are greater than the value of their parent (root) node's value.

**Note:** A subtree must include all of its descendants.

**Follow up:** Can you figure out ways to solve it with O(n) time complexity?

 

**Example 1:**

![333_tmp.jpg](img/333_tmp.jpg)
```
Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
```

**Example 2:**
```
Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `-10^4 <= Node.val <= 10^4`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 52 ms
Memory Usage: 16.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, float('inf'), float('-inf')
            left_n, left_min, left_max = dfs(node.left)
            right_n, right_min, right_max = dfs(node.right)
            if left_max < node.val < right_min:
                ans = max(ans, left_n + right_n + 1)
                left_min = node.val if left_min == float('inf') else left_min
                right_max = node.val if right_max == float('-inf') else right_max
                return left_n+right_n+1, left_min, right_max
            else:
                return 0, float('-inf'), float('inf')
            
        dfs(root)
        return ans
```