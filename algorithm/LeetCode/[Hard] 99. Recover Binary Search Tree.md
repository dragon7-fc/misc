99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

**Example 1:**
```
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
```

**Example 2:**
```
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

**Follow up:**

* A solution using `O(n)` space is pretty straight forward.
* Could you devise a constant space solution?

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 80 ms
Memory Usage: 14.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            #spot node which is out of order
            #the first appearing swaped node must be greater than the next node 
            if not self.first and node.val < self.pre.val: self.first = self.pre
            #the second appearing swaped node must be smaller than the pre node
            if self.first and node.val < self.pre.val: self.second = node
            self.pre = node
            inorder(node.right)
            
        self.pre, self.first, self.second = TreeNode(-float('inf')), None, None
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
```

**Solution 2: (DFS, in-order)**
```
Runtime: 52 ms
Memory Usage: 53.6 MB
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
    TreeNode *first, *second, *prev;
    void traverse(TreeNode* root)
    {
        if (root == nullptr)
            return;
        traverse(root->left);
        
        if (first == nullptr && prev->val > root->val)
            first = prev;
        if (first != nullptr && prev->val > root->val)
            second = root;
        prev = root;
        traverse(root->right);
        
    }
public:
    void recoverTree(TreeNode* root) {
        first = nullptr;
        second = nullptr;
        prev = new TreeNode(INT_MIN);
        traverse(root);
        swap(first->val, second->val);
    }
};
```
