1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 

**Example 1:**

![1302_1483_ex1.png](img/1302_1483_ex1.png)
```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```

**Constraints:**

* The number of nodes in the tree is between `1` and `10^4`.
* The value of nodes is between `1` and `100`.

# Submissions
---
**Solution 1: (BFS)**

**Explanation**

* `pre` are nodes in the previous level.
* `l` are node in the current level.

* When current level are empty,the previous level are the deepest leaves.


**Complexity**
* Time O(N)
* Space O(N)

```
Runtime: 80 ms
Memory Usage: 16.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        l = [root]
        while l:
            pre, l = l, [child for p in l for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
```

**Solution 2: (BFS)**
```
Runtime: 126 ms
Memory Usage: 61.9 MB
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
    int deepestLeavesSum(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        int sz, ans;
        while (!q.empty()) {
            sz = q.size();
            ans = 0;
            for (int i = 0; i < sz; i ++) {
                cur = q.front();
                q.pop();
                ans += cur->val;
                if (cur->left)
                    q.push(cur->left);
                if (cur->right)
                    q.push(cur->right);
            }
        }
        return ans;
    }
};
```
