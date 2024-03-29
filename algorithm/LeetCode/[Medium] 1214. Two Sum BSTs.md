1214. Two Sum BSTs

Given two binary search trees, return `True` if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer `target`.

**Example 1:**

![1214_1368_1_a2](img/1214_1368_1_a2.png)

```
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
```

**Example 2:**

![1214_1368_2_a](img/1214_1368_2_a.png)

```
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
```

**Constraints:**

* Each tree has at most 5000 nodes.
* `-10^9 <= target`, `node.val <= 10^9`

# Submissions
---
**Solution 1: (Binary Search Tree, DFS)**
```
Runtime: 1372 ms
Memory Usage: 18.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        from functools import lru_cache
        @lru_cache()
        def dfs(n1, n2):
            if not n1 or not n2:
                return False
            if n1.val + n2.val < target:
                return dfs(n1.right, n2) or dfs(n1, n2.right)
            elif n1.val + n2.val > target:
                return dfs(n1.left, n2) or dfs(n1, n2.left)
            else:
                return True
        return dfs(root1, root2)
```

**Solution 2: (Binary Search Tree, DFS)**
```
Runtime: 520 ms
Memory Usage: 21.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))
```

**Solution 3: (Set)**
```
Runtime: 28 ms
Memory: 36.7 MB
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
    void dfs(TreeNode *node, unordered_set<int> &st) {
        if (!node) {
            return;
        }
        st.insert(node->val);
        dfs(node->left, st);
        dfs(node->right, st);
    }
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        unordered_set<int> st, st2;
        dfs(root1, st);
        dfs(root2, st2);
        for (int a: st) {
            if (st2.count(target-a)) {
                return true;
            }
        }
        return false;
    }
};
```
