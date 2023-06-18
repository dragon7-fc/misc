530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

**Example:**
```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```

**Note:** There are at least two nodes in this BST.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 56 ms
Memory Usage: 14.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        v = []
        def dfs(node):
            nonlocal v
            if not node:
                return
            dfs(node.left)
            v += [node.val]
            dfs(node.right)
            
        dfs(root)
        return min([v[i] - v[i-1] for i in range(1, len(v))])
```

**Solution 2: (DFS)**
```
Runtime: 23 ms
Memory: 25.3 MB
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
    TreeNode* pre = nullptr;
    void dfs(TreeNode *cur, int &ans) {
        if (cur->left) {
            dfs(cur->left, ans);
        }
        if (pre) {
            ans = min(ans, cur->val - pre->val);
        }
        pre = cur;
        if (cur->right) {
            dfs(cur->right, ans);
        }

    }
public:
    int getMinimumDifference(TreeNode* root) {
        int ans = INT_MAX;
        dfs(root, ans);
        return ans;
    }
};
```
