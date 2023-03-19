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
Runtime: 11 ms
Memory: 26 MB
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
    TreeNode* dfs(int left, int right, int &pi, vector<int>& inorder, vector<int>& postorder) {
        if (left > right) {
            return nullptr;
        }
        int mid;
        for (int i = right; i >= 0; i --) {
            if (inorder[i] == postorder[pi]) {
                mid = i;
                break;
            }
        }
        TreeNode* node = new TreeNode(inorder[mid]);
        pi -= 1;
        node->right = dfs(mid+1, right, pi, inorder, postorder);
        node->left = dfs(left, mid-1, pi, inorder, postorder);
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int pi = postorder.size()-1;
        return dfs(0, postorder.size()-1, pi, inorder, postorder);
    }
};
```
