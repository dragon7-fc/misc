104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 40 ms
Memory Usage: 14.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

**Solution 2: (DFS)**
```
Runtime: 8 ms
Memory Usage: 19.3 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        
        int left;
        int right;
        
        left = maxDepth(root->left);
        right = maxDepth(root->right);
        
        return (max(left,right))+1;
    }
};
```

**Solution 3: (BFS)**
```
Runtime: 40 ms
Memory Usage: 15.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = [[root, 1]] if root else []
        depth = 0
        while q:
            node, d = q.pop(0)
            depth = max(depth, d)
            for c in [node.left, node.right]:
                if c:
                    q += [[c, d+1]]
            
        return depth
```