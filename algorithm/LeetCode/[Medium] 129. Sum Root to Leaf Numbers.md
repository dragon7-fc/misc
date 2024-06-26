129. Sum Root to Leaf Numbers

Given a binary tree containing digits from `0-9` only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path `1->2->3` which represents the number `123`.

Find the total sum of all root-to-leaf numbers.

**Note:** A leaf is a node with no children.

**Example:**
```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```
**Example 2:**
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 24 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, total):
            nonlocal ans
            if not node.left and not node.right:
               ans += total
            
            if node.left:
                dfs(node.left, total*10 + node.left.val)
            if node.right:
                dfs(node.right, total*10 + node.right.val)
            return
            
        if not root:
            return 0
        dfs(root, root.val)
        return ans
```

**Solution 2: (DFS)**
```
```
Runtime: 0 ms
Memory: 10.77 MB
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
    int dfs(TreeNode* node, int cur) {
        if (!node) {
            return 0;
        }
        cur = cur*10 + node->val;
        if (!node->left && !node->right) {
            return cur;
        }
        return dfs(node->left, cur) + dfs(node->right, cur);
    }
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
};
```
