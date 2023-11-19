124. Binary Tree Maximum Path Sum

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

**Example 1:**
```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**
```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 84 ms
Memory Usage: 21.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            rst = node.val + max(left, right)
            ans = max(ans, node.val+left+right)
            return max(rst, 0)
        
        dfs(root)
        return ans
```

**Solution 2: (DFS, no global variable)**
```
Runtime: 152 ms
Memory Usage: 21.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        Status = collections.namedtuple('Status', ('max_path_sum', 'max_until_node'))
        
        def helper(node):
            if not node:
                return Status(float('-inf'), 0)
            
            l_status = helper(node.left)
            r_status = helper(node.right)
            
            max_path_sum = max(l_status.max_path_sum, 
                                  r_status.max_path_sum,
                                  node.val + max(l_status.max_until_node, 0) + max(r_status.max_until_node, 0))
            
            max_until_node = max(node.val + max(l_status.max_until_node, 0),  
                                 node.val + max(r_status.max_until_node, 0))
            
            return Status(max_path_sum, max_until_node)
    
        return helper(root).max_path_sum
```

**Solution 3: (DFS)**
```
Runtime: 16 ms
Memory Usage: 13.6 MB
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
int dfs(struct TreeNode* node, int *rst) {
    if (!node)
        return 0;
    int left, right, res;
    left = dfs(node->left, rst);
    right = dfs(node->right, rst);
    res = node->val + (left > right ? left : right);
    *rst = (*rst < node->val+left+right ? node->val+left+right : *rst);
    return res > 0 ? res : 0;
}

int maxPathSum(struct TreeNode* root){
    int ans = INT_MIN;
    dfs(root, &ans);
    return ans;
}
```

**Solution 4: (DFS)**
```
Runtime: 219 ms
Memory: 21.5 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        # post order traversal of subtree rooted at `node`
        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            if not node:
                return 0

            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gain_from_left = max(gain_from_subtree(node.left), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            # return the max sum for a path starting at the root of subtree
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return max_path
```

**Solution 5: (DFS)**
```
Runtime: 12 ms
Memory: 27.9 MB
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
    int ans = 0;
    int dfs(TreeNode* node, int &ans) {
        if (!node) {
            return 0;
        }
        int left = dfs(node->left, ans);
        int right = dfs(node->right, ans);
        ans = max(ans, node->val + left + right);
        return max(node->val + max(left, right), 0);
    }
public:
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        dfs(root, ans);
        return ans;
    }
};
```
