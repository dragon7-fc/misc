513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

**Example 1:**
```
Input:

    2
   / \
  1   3

Output:
1
```

**Example 2**
```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
```

**Note:** You may assume the tree (i.e., the given root node) is not **NULL**.

# Submissions
---
**Solution 1: (BFS)**
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        res = None
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            else:
                res = node.val
        return res
```

**Solution 2: (BFS)**
```
Runtime: 17 ms
Memory Usage: 21.7 MB
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
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*>q;
        TreeNode* node;
        int ans;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i ++) {
                node = q.front();
                q.pop();
                if (node->right)
                    q.push(node->right);
                if (node->left)
                    q.push(node->left);
                else
                    ans = node->val;
            }
        }
        return ans;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 7 ms
Memory: 20.02 MB
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
    int findBottomLeftValue(TreeNode* root) {
        stack<pair<TreeNode*, int>> stk;
        stk.push({root, 0});
        TreeNode *node;
        int mx_row = -1, ans;
        while (stk.size()) {
            auto [node, row] = stk.top();
            stk.pop();
            if (row > mx_row) {
                mx_row = row;
                ans = node->val;
            }
            if (node->right) {
                stk.push({node->right, row+1});
            }
            if (node->left) {
                stk.push({node->left, row+1});
            }
        }
        return ans;
    }
};
```
