98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys **less** than the node's key.
* The right subtree of a node contains only nodes with keys **greater** than the node's key.
* Both the left and right subtrees must also be binary search trees.
 

**Example 1:**
```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

**Example 2:**
```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 44 ms
Memory Usage: 15 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, low, high):    
            if not node: return True       
            if node.val >= high or node.val <= low: return False      
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            
        return dfs(root, float('-inf'), float('inf'))
```

**Solution 2: (DFS)**
```
Runtime: 24 ms
Memory Usage: 21.5 MB
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
    bool dfs(TreeNode* node, long low, long high) {
        if (!node)
        {
            return true;
        }
        if (node->val >= high || node->val <= low)
        {
            return false;
        }
        return dfs(node->left, low, node->val) && dfs(node->right, node->val, high);
    }
    bool isValidBST(TreeNode* root) {
        return dfs(root, LLONG_MIN, LLONG_MAX);
    }
};
```