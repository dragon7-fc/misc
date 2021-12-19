543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.

**Example:**
```
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Note:** The length of path between two nodes is represented by the number of edges between them.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition**

Any path can be written as two arrows (in different directions) from some node, where an arrow is a path that starts at some node and only travels down to child nodes.

If we knew the maximum length arrows `L`, `R` for each child, then the best path touches `L + R + 1` nodes.

**Algorithm**

Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node and remember the highest number of nodes used in some path. The desired length is 1 minus this number.

```python
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
```

**Complexity Analysis**

* Time Complexity: $O(N)$. $W$ visit every node once.

* Space Complexity: $O(N)$, the size of our implicit call stack during our depth-first search.

# Submissions
---
**Solution 1: (Depth-First Search)**
```
Runtime: 44 ms
Memory Usage: 14.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
```

**Solution 2: (DFS)**
```
Runtime: 4 ms
Memory Usage: 7.9 MB
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
int dfs(struct TreeNode *node, int *rst) {
    if (!node)
        return 0;
    int left, right;
    left = dfs(node->left, rst);
    right = dfs(node->right, rst);
    *rst = (*rst < left+right ? left+right : *rst);
    return 1 + (left > right ? left : right);
}

int diameterOfBinaryTree(struct TreeNode* root){
    int ans = 0;
    dfs(root, &ans);
    return ans;
}
```
