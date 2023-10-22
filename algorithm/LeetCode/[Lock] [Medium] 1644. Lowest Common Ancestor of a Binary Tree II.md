1644. Lowest Common Ancestor of a Binary Tree II

Given the `root` of a binary tree, return the lowest common ancestor (LCA) of two given nodes, `p` and `q`. If either node `p` or `q` **does not exist** in the tree, return `null`. All values of the nodes in the tree are **unique**.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes `p` and `q` in a binary tree T is the lowest node that has both `p` and `q` as **descendants** (where we allow **a node to be a descendant of itself**)". A **descendant** of a node `x` is a node `y` that is on the path from node `x` to some leaf node.

 

**Example 1:**

![1644_binarytree.png](img/1644_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

![1644_binarytree.png](img/1644_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
```

**Example 3:**


```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-10^9 <= Node.val <= 10^9`
* All Node.val are unique.
* `p != q`
 

**Follow up:** Can you find the LCA traversing the tree, without checking nodes existence?

# Submissions
---
**Solution 1: (DFS, Post-Order)**
```
Runtime: 304 ms
Memory Usage: 29 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def dfs(node):
            nonlocal ans
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right or ((left or right) and node in [p, q]):
                ans = node
            elif left or right:
                return left or right
            elif node in [p, q]:
                return node
                
        dfs(root)
        return ans
```

**Solution 2: (DFS, post order)**
```
Runtime: 95 ms
Memory: 64.2 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        bool nodesFound = false;

        function<TreeNode*(TreeNode*)> dfs = [&](TreeNode* node) {
            if (!node)
              return node;
            TreeNode* left = dfs(node->left);
            TreeNode* right = dfs(node->right);
            int conditions = 0;
            if (node == p || node == q)
              conditions++;
            if (left != NULL)
              conditions++;
            if (right != NULL)
              conditions++;
            if (conditions == 2)
              nodesFound = true;
            
            if ((left && right) || (node == p) || (node == q))
              return node;
            return left ? left : right;
        };

        TreeNode* ans = dfs(root);
        return nodesFound ? ans : NULL;
    }
};
```
