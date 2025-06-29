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

**Solution 2: (DFS, pre-order)**
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

**Solution 3: (DFS, pre-order)**
```
Runtime: 8 ms
Memory Usage: 8.6 MB
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
bool *dfs(struct TreeNode *node, long low, long high) {
    if (!node)
        return true;
    if (node->val >= high || node->val <= low)
        return false;
    return dfs(node->left, low, node->val) && dfs(node->right, node->val, high);
}

bool isValidBST(struct TreeNode* root){
    return dfs(root, LLONG_MIN, LLONG_MAX);
}
```

**Solution 5: (DFS, postorder)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 23.09 MB, Beats 9.31%
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
    pair<long long,long long> dfs(TreeNode *node, bool &ans) {
        if (!node) {
            return {LONG_LONG_MAX, LONG_LONG_MIN};
        }
        if (!node->left && !node->right) {
            return {node->val, node->val};
        } 
        if (!ans) {
            return {LONG_LONG_MAX, LONG_LONG_MIN};
        }
        long long lleft, lright, rleft, rright;
        auto pa = dfs(node->left, ans);
        lleft = pa.first;
        lright = pa.second;
        auto pb = dfs(node->right, ans);
        rleft = pb.first;
        rright = pb.second;
        if (node->val <= lright || node->val >= rleft) {
            ans = false;
        } 
        return {min({lleft, rleft, (long long)node->val}), max({lright, rright, (long long)node->val})};
    }
public:
    bool isValidBST(TreeNode* root) {
        bool ans = true;
        dfs(root, ans);
        return ans;
    }
};
```

**Solution 5: (DFS, preorder)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 21.94 MB, Beats 46.44%
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
    bool dfs(TreeNode *node, long long left, long long right) {
        if (!node) {
            return true;
        }
        if (node->val <= left || node->val >= right) {
            return false;
        } 
        if (node->left && !dfs(node->left, left, node->val)) {
            return false;
        }
        if (node->right && !dfs(node->right, node->val, right) ) {
            return false;
        }
        return true;
    }
public:
    bool isValidBST(TreeNode* root) {
        return dfs(root, LONG_LONG_MIN, LONG_LONG_MAX);
    }
};
```
