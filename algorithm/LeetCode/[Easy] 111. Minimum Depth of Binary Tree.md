111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its minimum depth = 2.

# Submissions
---
**Solution 1: (DFS)**
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
    def minDepth(self, root: TreeNode) -> int:
        self.depth = float('Inf')
        def dfs(node, depth):
            if not node:return
            if not node.right and not node.left:
                self.depth = min(self.depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        if not root:return 0
        dfs(root, 1)
        return self.depth
```

**Solution 2: (BFS)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = collections.deque()
        q.append((root,1))
        
        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
                return level
            
            for node in [node.left, node.right]:
                if node:
                    q.append((node, level+1))
```

**Solution 3: (DFS)**
```
Runtime: 596 ms
Memory Usage: 53.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: 
            return 0
        if root.left == None and root.right == None: # Reach leaf node
            return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

**Solution 4: (DFS)**
```
Runtime: 224 ms
Memory Usage: 144.9 MB
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
    int minDepth(TreeNode* root) {
        if (!root)
            return 0;
        if (!root->left && !root->right)
            return 1;
        if (!root->left)
            return 1 + minDepth(root->right);
        if (!root->right)
            return 1 + minDepth(root->left);
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};
```

**Solution 5: (BFS)**
```
Runtime: 288 ms
Memory: 144.6 MB
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
    int minDepth(TreeNode* root) {
        if (!root) {
            return 0;
        }
        queue<TreeNode*> q;
        q.push(root);
        int ans = 1, sz;
        TreeNode *cur;
        while (!q.empty()) {
            sz = q.size();
            for (int i = 0; i < sz; i ++) {
                cur = q.front();
                q.pop();
                if (!cur->left && !cur->right) {
                    return ans;
                }
                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
            }
            ans += 1;
        }
        return ans;
    }
};
```
