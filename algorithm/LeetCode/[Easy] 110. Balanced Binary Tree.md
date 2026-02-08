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

**Solution 2: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 23.07 MB, Beats 54.19%
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
    pair<bool, int> dfs(TreeNode *node) {
        if (!node) {
            return {true, 0};
        }
        auto [is_left, left] = dfs(node->left);
        auto [is_right, right] = dfs(node->right);
        return {is_left && is_right && abs(left - right) <= 1, 1 + max(left, right)};
    }
public:
    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }
};
```
