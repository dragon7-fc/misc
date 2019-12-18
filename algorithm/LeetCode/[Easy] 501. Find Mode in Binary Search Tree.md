501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
* The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
* Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST `[1,null,2,2]`,
```
   1
    \
     2
    /
   2
```

return [2].

**Note:** If a tree has more than one mode, you can return them in any order.

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Submissions
---
**Solution 1:**
```
Runtime: 52 ms
Memory Usage: 16.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(node, count):
            if not node:
                return []
            
            count[node.val] += 1
            dfs(node.left, count)
            dfs(node.right, count)
            return
        
        counter = collections.defaultdict(int)
        dfs(root, counter)
        most_freq = max(counter.values()) if counter else -1
        ans = []
        for k in counter.keys():
            if counter[k] == most_freq:
                ans += [k]
        return ans
```