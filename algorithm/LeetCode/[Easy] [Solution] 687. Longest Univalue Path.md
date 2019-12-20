687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

**Example 1:**
```
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2
```

**Example 2:**
```
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2
```
 

**Note:** The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# Solution
---
## Approach #1: Recursion [Accepted]
**Intuition**

We can think of any path (of nodes with the same values) as up to two arrows extending from it's root.

Specifically, the root of a path will be the unique node such that the parent of that node does not appear in the path, and an arrow will be a path where the root only has one child node in the path.

Then, for each node, we want to know what is the longest possible arrow extending left, and the longest possible arrow extending right? We can solve this using recursion.

**Algorithm**

Let `arrow_length(node)` be the length of the longest arrow that extends from the `node`. That will be `1 + arrow_length(node.left)` if `node.left` exists and has the same value as node. Similarly for the `node.right` case.

While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node. We record these candidate answers and return the best one.

```python
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the tree. We process every node once.

* Space Complexity: $O(H)$, where $H$ is the height of the tree. Our recursive call stack could be up to $H$ layers deep.

# Submissions
---
**Solution:**
```
Runtime: 428 ms
Memory Usage: 16.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
```