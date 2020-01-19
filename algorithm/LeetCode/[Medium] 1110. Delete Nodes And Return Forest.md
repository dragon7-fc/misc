1110. Delete Nodes And Return Forest

Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

**Example 1:**


```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

**Constraints:**

1. The number of nodes in the given tree is at most `1000`.
1. Each node has `a` distinct value between `1` and `1000`.
1. `to_delete.length <= 1000`
1. `to_delete` contains distinct values between `1` and `1000`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 56 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        del_set = set(to_delete) 
        def dfs(root,res,del_set):
            if not root:
                return None
            root.left = dfs(root.left,res,del_set)
            root.right = dfs(root.right,res,del_set)
            # process root
            if root.val not in del_set:
                return root
            else:
                if root.left: res.append(root.left)
                if root.right: res.append(root.right)
                return None
            
        res = []
        root = dfs(root,res,del_set)
        if root:
            res.append(root)
        return res
```