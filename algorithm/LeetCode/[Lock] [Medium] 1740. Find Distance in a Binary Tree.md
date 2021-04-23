1740. Find Distance in a Binary Tree

Given the `root` of a binary tree and two integers `p` and `q`, return the distance between the nodes of value `p` and value `q` in the tree.

The **distance** between two nodes is the number of edges on the path from one to the other.

 

**Example 1:**

![1740_binarytree.png](img/1740_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
```

**Example 2:**

![1740_binarytree.png](img/1740_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.
```

**Example 3:**

![1740_binarytree.png](img/1740_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `0 <= Node.val <= 10^9`
* All Node.val are **unique**.
* `p` and `q` are values in the tree.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 96 ms
Memory Usage: 27.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if not root: return 0

        def lca(node, p, q):
            if not node: return
            if node.val == p or node.val == q:
                return node
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if left and right: return node
            return left if left else right

        def dfs(node, target, dist):
            if not node: return 0
            if node.val == target:
                return dist
            left = dfs(node.left, target, dist + 1)
            right = dfs(node.right, target, dist + 1)
            return left if left else right

        node = lca(root, p, q)
        if node.val == root.val:
            return dfs(root, p, 0) + dfs(root, q, 0)
        else:
            return abs(dfs(root, q, 0) - dfs(root, p, 0))
```