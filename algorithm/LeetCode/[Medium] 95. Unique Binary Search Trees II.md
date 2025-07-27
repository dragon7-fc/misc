95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique **BST**'s (binary search trees) that store values 1 ... n.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Submissions:
---
**Solution 1: (DP Top-Down)**
```
Runtime: 56 ms
Memory Usage: 13.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        @functools.lru_cache(None)
        def dfs(l, r):   # split between [l, r)
            if l == r:
                return [None]  # list contain None object
            rst = []
            for i in range(l, r):
                for lchild in dfs(l, i):
                    for rchild in dfs(i+1, r):
                        root = TreeNode(i+1)   # +1 to convert the index to the actual value
                        root.left = lchild
                        root.right = rchild
                        rst.append(root)
            return rst
        
        return dfs(0, n) if n else []
```

**Solution 2: (Backtracking)**
```
Runtime: 17 ms
Memory: 16.7 MB
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
    vector<TreeNode*> generateTrees(int end, int start = 1) {
        vector<TreeNode*> ans;       
        // If start > end, then subtree will be empty so we will directly return null pointer
        if (start> end)
            return {nullptr};
        
        // Consider every number in range [start, end] as root
        for (int i = start; i <= end; i++) {
            // generate all possible trees in range [start, i)
            for (auto left : generateTrees(i - 1, start)) {
                // generate all possible trees in range (i, end]
                for (auto right : generateTrees(end, i + 1))
                    // make new trees with 'i' as the root
                    ans.push_back(new TreeNode(i, left, right));
            }
        }
        return ans;
    }
};
```

**Solution 3: (DP, Top-Down)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.11 MB, Beats 79.63%
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
    vector<TreeNode*> dfs(int left, int right, vector<vector<vector<TreeNode*>>> &dp) {
        if (left > right) {
            return {nullptr};
        }
        if (dp[left-1][right-1].size()) {
            return dp[left-1][right-1];
        }
        vector<TreeNode*> rst;
        TreeNode *node;
        for (int a = left; a <= right; a ++) {
            for (auto nl: dfs(left, a-1, dp)) {
                for (auto nr: dfs(a+1, right, dp)) {
                    node = new TreeNode(a);
                    node->left = nl;
                    node->right = nr;
                    rst.push_back(node);
                }
            }
        }
        dp[left-1][right-1] = rst;
        return rst;
    }
public:
    vector<TreeNode*> generateTrees(int n) {
        vector<vector<vector<TreeNode*>>> dp(n, vector<vector<TreeNode*>>(n));
        return dfs(1, n, dp);
    }
};
```
