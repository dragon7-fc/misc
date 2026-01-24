105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
Runtime: 160 ms
Memory Usage: N/A
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
```

**Solution 2: (DFS)**
```
Runtime: 36 ms
Memory Usage: 23.2 MB
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
    TreeNode* dfs(vector<int>& preorder, vector<int>& inorder, int start, int end, int& root) {
        if (start > end) return NULL;
        int mid = start;
        for (int i=start;i<=end;i++) {
            if (preorder[root] == inorder[i]){
                mid = i;
                break;
            }
        }
        return new TreeNode(preorder[root++],
                            dfs(preorder, inorder, start, mid-1, root),
                            dfs(preorder, inorder, mid+1, end, root));
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int root = 0;
        return dfs(preorder, inorder, 0, preorder.size()-1, root);
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 16 ms
Memory Usage: 11.6 MB
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
struct TreeNode* dfs(int *preorder, int *p_index, int size, int *inorder, int left, int right) {
    if (left > right)
        return NULL;
    struct TreeNode *node = malloc(sizeof(struct TreeNode));;
    node->val = preorder[*p_index];
    *p_index += 1;
    if (left == right){
        node->left = NULL;
        node->right = NULL;
        return node;
    }
    for (int i = left; i <= right; i ++) {
        if (inorder[i] == node->val) {
            node->left = dfs(preorder, p_index, size, inorder, left, i-1);
            node->right = dfs(preorder, p_index, size, inorder, i+1, right);
            break;
        }
    }
    return node;
}

struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize){
    int p_index = 0;
    return dfs(preorder, &p_index, preorderSize, inorder, 0, inorderSize-1);
}
```

**Solution 4: (DFS)**

    preorder = [ 3, 9,20,15, 7], inorder = [9,3,15,20,7]
                 ^                         [ ]m[       ]
                    ^                      [ ]
                      ^                        [   ]m[ ]
                         ^                     [   ]
                            ^                        [ ]
                    3
                  /    \
                 9     20
                      /  \
                    15    7

```
Runtime: 6 ms, Beats 42.87%
Memory: 27.05 MB, Beats 89.98%
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
    TreeNode *dfs(int &i, int left, int right, vector<int> &preorder, vector<int> &inorder) {
        if (left > right) {
            return nullptr;
        }
        TreeNode *node = new TreeNode(preorder[i]);
        i += 1;
        if (left == right) {
            return node;
        }
        int mid = find(inorder.begin() + left, inorder.end(), node->val) - inorder.begin();
        node->left = dfs(i, left, mid-1, preorder, inorder);
        node->right = dfs(i, mid+1, right, preorder, inorder);
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int i = 0;
        return dfs(i, 0, inorder.size()-1, preorder, inorder);
    }
};
```
