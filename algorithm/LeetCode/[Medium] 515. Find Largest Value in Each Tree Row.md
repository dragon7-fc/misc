515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

**Example:**
```
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
```

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 36 ms
Memory Usage: 14.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        level = root and [root]
        ans = []
        while level:
            ans.append(max([node.val for node in level]))
            level = [c for node in level for c in [node.left, node.right] if c]
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 12 ms
Memory Usage: 22 MB
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
    vector<int> largestValues(TreeNode* root) {
        if (!root) return vector<int>();
        vector<int> ans;
        queue<TreeNode*> q;
        TreeNode* node;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            int cur = INT_MIN;
            for (int i = 0; i < sz; i ++) {
                node = q.front();
                q.pop();
                cur = max(cur, node->val);
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            ans.push_back(cur);
        }
        return ans;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 0 ms
Memory: 22.60 MB
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
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) {
            return vector<int>{};
        }
        vector<int> ans;
        stack<pair<TreeNode*, int>> stk;
        stk.push({root, 0});
        while (!stk.empty()) {
            auto [node, d] = stk.top();
            stk.pop();
            if (d == ans.size()) {
                ans.push_back(node->val);
            } else {
                ans[d] = max(ans[d], node->val);
            }
            if (node->left) {
                stk.push({node->left, d + 1});
            }
            if (node->right) {
                stk.push({node->right, d + 1});
            }
        }
        return ans;
    }
};
```
