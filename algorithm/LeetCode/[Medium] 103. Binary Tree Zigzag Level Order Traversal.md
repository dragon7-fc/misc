103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
]
```

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 36 ms
Memory Usage: 14.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = root and [root]
        ans = []
        forward = True
        while level:
            if forward:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level[::-1]])
            level = [c for node in level for c in [node.left, node.right] if c]
            forward = not forward
        
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 0 ms
Memory Usage: 12.4 MB
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        vector<vector<int>> res;
        while(!q.empty()){
            int sz = q.size(); 
            vector<int> curr(sz);
            for(int i = 0; i < sz; i++){
                TreeNode* temp = q.front();
                q.pop();
                if(level == 0){
                    curr[i] = temp->val;
                }else{
                    curr[sz - i - 1] = temp->val;
                }
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            level = level == 0 ? 1 : 0;
            res.push_back(curr);
        }
        return res;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 8 ms
Memory Usage: 12.4 MB
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        int l2r = 1;
        vector<vector<int>>res;
        stack<TreeNode*> current, next;
        
        current.push(root);
        
        TreeNode *temp;
        vector<int> v;
        
        while(!current.empty()) {
            temp = current.top();
            current.pop();
            if(temp) {
                v.push_back(temp->val);
                if(l2r) {
                    if(temp->left)   next.push(temp->left);
                    if(temp->right)  next.push(temp->right);
                }
                else {
                    if(temp->right)  next.push(temp->right);
                    if(temp->left)   next.push(temp->left);
                }
            }
            if(current.empty())
            {
                l2r = 1 - l2r;
                res.push_back(v);
                swap(current, next);
                v.clear();
            }
        }
       
        return res;
    }
};
```