106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

For example, given
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:
```
   3
   / \
  9  20
    /  \
   15   7
```

# Submissions
---
**Solution 1: (DFS, Tree, Post-Order)**
```
Runtime: 140 ms
Memory Usage: 53 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
```

**Solution 2: (DFS)**
```
Runtime: 56 ms
Memory Usage: 220.9 MB
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
    TreeNode* create(vector<int> inor, vector<int> post, int is, int ie, int ps, int pe){
        if(ps>pe)
            return NULL;
        TreeNode* node=new TreeNode(post[pe]);
        int k=0;
        for (int i = is; i <= ie; i++){
            if (inor[i] == post[pe]){
                k = i;
                break;
            }
        }
        node->left=create(inor, post, is, k-1, ps, ps+k-is-1);
        node->right=create(inor, post, k+1, ie, pe-ie+k, pe-1);
        return node;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return create(inorder, postorder, 0, inorder.size()-1, 0, postorder.size()-1);
    }
};
```