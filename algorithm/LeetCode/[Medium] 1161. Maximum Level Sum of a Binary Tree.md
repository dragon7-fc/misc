1161. Maximum Level Sum of a Binary Tree

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `X` such that the sum of all the values of nodes at level `X` is **maximal**.

 

**Example 1:**


```
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

**Note:**

* The number of nodes in the given tree is between `1` and `10^4`.
* ``-10^5 <= node.val <= 10^5`

# Submissions
---
**Solution 1: (BFS, Level-order, Tree)**
```
Runtime: 320 ms
Memory Usage: 17.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = [root]
        ans = [float('-inf'), 0]  # level sum, level
        lv = 1
        while level:
            sm = sum([node.val for node in level])
            if sm > ans[0]:
                ans = [sm, lv]
            level = [c for node in level if node for c in [node.left, node.right] if c]
            lv += 1
            
        return ans[1]
```

**Solution 2: (BFS, Level-order, Tree)**
```
Runtime: 206 ms
Memory: 107.2 MB
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
    int maxLevelSum(TreeNode* root) {
        queue<TreeNode*> q;
        int ans = 0, cur = 0, mx = INT_MIN, vals, sz;
        q.push(root);
        while (!q.empty()) {
            sz = q.size();
            vals = 0;
            cur += 1;
            for (int i = 0; i < sz; i ++) {
                vals += q.front()->val;
                if (q.front()->left) {
                    q.push(q.front()->left);
                }
                if (q.front()->right) {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            if (vals > mx) {
                mx = vals;
                ans = cur;
            }
        }
        return ans;
    }
};
```
