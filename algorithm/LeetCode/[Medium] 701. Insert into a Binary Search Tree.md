701. Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 
```
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
```
You can return this binary search tree:
```
         4
       /   \
      2     7
     / \   /
    1   3 5
```
This tree is also valid:
```
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
```

# Submissions
---
**Solution 1: (DFS, Iterative)**
```
Runtime: 116 ms
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        new = TreeNode(val)
        while node != None:
            prev = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
                
        if prev.val > val:
            prev.left = new
        else:
            prev.right = new
        return root
```

**Solution 2: (DFS, Recursive)**
```
Runtime: 132 ms
Memory Usage: 16.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        else:
            if root.val > val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root
```

**Solution 3: (DFS, Recursive)**
```
Runtime: 171 ms
Memory Usage: 57 MB
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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(!root) return new TreeNode(val);
        if(root->val > val) root->left = insertIntoBST(root->left, val);
        else root->right = insertIntoBST(root->right, val);
        return root;
    }
};
```

**Solution 4: (DFS, Recursive)**
```
Runtime: 117 ms
Memory Usage: 22.7 MB
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


struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    if (!root) {
        struct TreeNode* node = calloc(1, sizeof(struct TreeNode));
        node->val = val;
        return node;
    }
    if (root->val > val) 
        root->left = insertIntoBST(root->left, val);
    else
        root->right = insertIntoBST(root->right, val);
    return root;
}
```
