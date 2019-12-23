971. Flip Binary Tree To Match Preorder Traversal

Given a binary tree with `N` nodes, each node has a different value from `{1, ..., N}`.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of `N` values reported by a preorder traversal starting from the root.  Call such a sequence of `N` values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the `voyage` we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list `[-1]`.

 

**Example 1:**


```
Input: root = [1,2], voyage = [2,1]
Output: [-1]
```

**Example 2:**


```
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
```

**Example 3:**


```
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
```

**Note:**

1. `1 <= N <= 100`

# Solution
---
## Approach 1: Depth-First Search
**Intuition**

As we do a pre-order traversal, we will flip nodes on the fly to try to match our voyage with the given one.

If we are expecting the next integer in our voyage to be `voyage[i]`, then there is only at most one choice for path to take, as all nodes have different values.

**Algorithm**

Do a depth first search. If at any node, the node's value doesn't match the voyage, the answer is `[-1]`.

Otherwise, we know when to flip: the next number we are expecting in the voyage `voyage[i]` is different from the next child.

```python
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
```