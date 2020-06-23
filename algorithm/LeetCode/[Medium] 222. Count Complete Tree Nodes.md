222. Count Complete Tree Nodes

Given a **complete** binary tree, count the number of nodes.

**Note:**

**Definition of a complete binary tree** from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:**
```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 92 ms
Memory Usage: 19.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

**Solution 2: (DFS)**
```
Runtime: 48 ms
Memory Usage: 30.8 MB
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
    int cnt=0;
    int countNodes(TreeNode* root) {
        dfs(root);
        return cnt;
    }
    void dfs(TreeNode* root)
    {
        if(!root) return;  
        cnt++;  
        dfs(root->left);
        dfs(root->right); 
    }
};
```