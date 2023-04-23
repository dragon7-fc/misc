1372. Longest ZigZag Path in a Binary Tree

Given a binary tree `root`, a ZigZag path for a binary tree is defined as follow:

* Choose any node in the binary tree and a direction (right or left).
* If the current direction is right then move to the right child of the current node otherwise move to the left child.
* Change the direction from right to left or right to left.
* Repeat the second and third step until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest **ZigZag** path contained in that tree.

 

**Example 1:**

![1372_sample_1_1702.png](img/1372_sample_1_1702.png)
```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
```

**Example 2:**

![1372_sample_2_1702.png](img/1372_sample_2_1702.png)
```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
```

**Example 3:**
```
Input: root = [1]
Output: 0
```

**Constraints:**

* Each tree has at most `50000` nodes..
* Each node's value is between `[1, 100]`.

# Submissions
---
**Solution 1: (Post-Order)**
```
Runtime: 592 ms
Memory Usage: 61.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, direction):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left,'left')
            right = dfs(node.right,'right')
            res = max(res, left+1, right+1)
            return right+1 if direction == 'left' else left+1
         
        if not root:
            return 0
        dfs(root,'left')
        dfs(root,'right')
        
        return res-1
```

**Solution 2: (Pre-Order)**
```
Runtime: 177 ms
Memory: 94.1 MB
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
    void dfs(TreeNode* node, int left, int right, int &ans) {
        ans = max(ans, max(left, right));
        if (node->left) {
            dfs(node->left, right+1, 0, ans);
        }
        if (node->right) {
            dfs(node->right, 0, left+1, ans);
        }
    }
public:
    int longestZigZag(TreeNode* root) {
        int ans = 0;
        dfs(root, 0, 0, ans);
        return ans;
    }
};
```
