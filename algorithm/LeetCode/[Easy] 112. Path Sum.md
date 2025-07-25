112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**
```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 44 ms
Memory Usage: 14.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
```

**Solution 1: (DFS)**
```
Runtime: 8 ms
Memory Usage: 8.2 MB
```
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool hasPathSum(struct TreeNode* root, int targetSum){
    if (!root)
        return false;
    if (!root->left && !root->right) {
        if (targetSum - root->val == 0)
            return true;
        return false;
    }
    return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
}
```

**Solution 3: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 21.54 MB, Beats 34.19%
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
    bool dfs(TreeNode *node, int p, int target) {
        if (!node) {
            return false;
        }
        p += node->val;
        if (!node->left && !node->right) {
            return p == target;
        }
        return dfs(node->left, p, target) || dfs(node->right, p, target);
    }
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        return dfs(root, 0, targetSum);
    }
};
```
