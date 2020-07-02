107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 36 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            ans += [[node.val for node in level if node]]
            level = [c for node in level if node for c in [node.left, node.right] if c]
        return ans[::-1]
```

**Solution 2: (BFS)**
```
Runtime: 12 ms
Memory Usage: 12.7 MB
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> Q;
        Q.push(root);
        while (!Q.empty()){
            int n = Q.size();
            vector<int> nodes(n);
            for(int i = 0; i < n; ++i){
                TreeNode* node = Q.front();
                nodes[i] = node->val;
                Q.pop();
                if (node->left) Q.push(node->left);
                if (node->right) Q.push(node->right);
            }
            result.push_back(nodes);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```