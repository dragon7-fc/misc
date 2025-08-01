559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

**Example 1:**

![559_narytreeexample.png](img/559_narytreeexample.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
```

**Example 2:**

![559_sample_4_964.png](img/559_sample_4_964.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
```

**Constraints:**

* The depth of the n-ary tree is less than or equal to `1000`.
* The total number of nodes is between `[0, 10^4]`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 48 ms
Memory Usage: 14.4 MB
```
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(c) for c in root.children) if root.children else 1
```

**Solution 2: (BFS)**
```
Runtime: 36 ms
Memory Usage: 14.7 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        level = root and [root]
        while level:
            ans += 1
            level = [c for node in level for c in node.children if c]
        return ans
```

**Solution 3: (DFS)**
```
Runtime: 4 ms
Memory Usage: 8 MB
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


int maxDepth(struct TreeNode* root){
    if (!root)
        return 0;
    int left, right;
    left = maxDepth(root->left);
    right = maxDepth(root->right);
    return 1 + (left > right ? left : right);
}
```

**Solution 4: (DFS)**
```
Runtime: 8 ms, Beats 89.47%
Memory: 14.44 MB, Beats 72.16%
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) {
            return 0;
        }
        int rst = 0;
        for (auto c: root->children) {
            rst = max(rst, maxDepth(c));
        }
        return rst + 1;
    }
};
```
