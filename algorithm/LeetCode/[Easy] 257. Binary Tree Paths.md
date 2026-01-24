257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

**Example:**
```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(node, path):
            nonlocal ans
            if not node.left and not node.right:
                ans.append(path)
                return
            if node.left:
                dfs(node.left, '{}->{}'.format(path, node.left.val))
            if node.right:
                dfs(node.right, '{}->{}'.format(path, node.right.val))
            
        if not root:
            return ""
        dfs(root, str(root.val))
        return ans
```

**Solution 2: (DFS, post order)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 18.54 MB, Beats 10.18%
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
    vector<string> binaryTreePaths(TreeNode* root) {
        if (!root) {
            return {};
        }
        if (!root->left && !root->right) {
            return {to_string(root->val)};
        }
        vector<string> rst;
        for (auto &left: binaryTreePaths(root->left)) {
            rst.push_back(to_string(root->val) + "->" + left);
        }
        for (auto &right: binaryTreePaths(root->right)) {
            rst.push_back(to_string(root->val) + "->" + right);
        }
        return rst;
    }
};
```

**Solution 3: (DFS, Pre order)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.62 MB, Beats 61.36%
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
    void dfs(TreeNode *node, string path, vector<string> &ans) {
        if (!node->left && !node->right) {
            ans.push_back(path);
            return;
        }
        if (node->left) {
            dfs(node->left, path + "->" + to_string(node->left->val), ans);
        }
        if (node->right) {
            dfs(node->right, path + "->" + to_string(node->right->val), ans);
        }
    }
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        string path;
        vector<string> ans;
        path += to_string(root->val);
        dfs(root, path, ans);
        return ans;
    }
};
```
