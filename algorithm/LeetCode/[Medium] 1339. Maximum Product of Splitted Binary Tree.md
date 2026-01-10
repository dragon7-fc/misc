1339. Maximum Product of Splitted Binary Tree

Given a binary tree `root`. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo `10^9 + 7`.

 

**Example 1:**

![1343_sample_1_1699.png](img/1343_sample_1_1699.png)
```
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
```

**Example 2:**

![1343_sample_2_1699.png](img/1343_sample_2_1699.png)
```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

**Example 3:**
```
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
```

**Example 4:**
```
Input: root = [1,1]
Output: 1
```

**Constraints:**

* Each tree has at most 50000 nodes and at least `2` nodes.
* Each node's value is between `[1, 10000]`.

# Submissions
---
**Sol;ution 1: (DFS)**

**Explanation**

* First pass, get the total sum
* Second pass, find the biggest product.


**Complexity**

* Time O(N)
* Space O(height)
We can save one pass if you we sacrifice moce space.

```
Runtime: 468 ms
Memory Usage: 77.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10**9 + 7
        self.res = total = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + node.val

        total = dfs(root)
        dfs(root)
        return self.res % MOD
```

**Solution 2: (DFS)**
```
Runtime: 408 ms
Memory Usage: 78.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def treesum(node):
            if not node: return 0
            return node.val + treesum(node.left) + treesum(node.right)
        
        def treemax(node, total):
            if not node: return 0
            l, r = treemax(node.left, total), treemax(node.right, total)
            self.rst = max(self.rst, l * (total-l), r * (total-r))
            return node.val + l + r
        
        total, self.rst = treesum(root), 0
        treemax(root, total)
        return self.rst % (10**9 + 7)
```

**Solution 3: (One Pass with Hash Set)**
```
Runtime: 816 ms
Memory: 77.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s = set()

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val + left + right
            s.add(cur)
            return cur
        
        total = dfs(root)
        ans = 0
        for v in s:
            ans = max(ans, (total-v)*v)
        return ans%(10**9 + 7)
```

**Solution 4: (DFS)**
```
Runtime: 3 ms, Beats 74.88%
Memory: 78.82 MB, Beats 32.16%
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
    void dfs(TreeNode *node, int &a) {
        if (!node) {
            return;
        }
        a += node->val;
        dfs(node->left, a);
        dfs(node->right, a);
    }
    int dfs2(TreeNode *node, int right, long long &ans) {
        if (!node) {
            return 0;
        }
        long long rst = node->val;
        rst += dfs2(node->left, right, ans);
        rst += dfs2(node->right, right, ans);
        ans = max(ans, (rst * (right - rst)));
        return rst;
    }
public:
    int maxProduct(TreeNode* root) {
        int right = 0, MOD = 1e9 + 7;
        long long ans = 0;
        dfs(root, right);
        dfs2(root, right, ans);
        return ans % MOD;
    }
};
```
