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
Runtime: 3 ms
Memory: 22.5 MB
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
            return {};
        }
        
        vector<int> ans;
        stack<pair<TreeNode*, int>> stack;
        stack.push({root, 0});
        
        while (!stack.empty()) {
            pair<TreeNode*, int> pair = stack.top();
            stack.pop();
            TreeNode* node = pair.first;
            int depth = pair.second;
            
            if (depth == ans.size()) {
                ans.push_back(node->val);
            } else {
                ans[depth] = max(ans[depth], node->val);
            }
            
            if (node->left) {
                stack.push(make_pair(node->left, depth + 1));
            }
            
            if (node->right) {
                stack.push(make_pair(node->right, depth + 1));
            }
        }
        
        return ans;
    }
};
```
