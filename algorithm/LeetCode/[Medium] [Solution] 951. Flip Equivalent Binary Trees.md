951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes `root1` and `root2`.

 

**Example 1:**
```
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
```
![951_tree_ex.png](img/951_tree_ex.png)

**Note:**

* Each tree will have at most `100` nodes.
* Each value in each tree will be a unique integer in the range `[0, 99]`.

# Solution
---
## Approach 1: Recursion
**Intuition**

If `root1` and `root2` have the same root value, then we only need to check if their children are equal (up to ordering.)

**Algorithm**

There are 3 cases:

* If `root1 `or `root2` is null, then they are equivalent if and only if they are both null.

* Else, if `root1` and `root2` have different values, they aren't equivalent.

* Else, let's check whether the children of `root1` are equivalent to the children of `root2`. There are two different ways to pair these children.

```python
class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
```

**Complexity Analysis**

* Time Complexity: $O(min(N_1, N_2))$, where $N_1, N_2$ are the lengths of `root1` and `root2`.

* Space Complexity: $O(min(H_1, H_2))$, where $H_1, H_2$ are the heights of the trees of `root1` and `root2`.

## Approach 2: Canonical Traversal
**Intuition**

Flip each node so that the left child is smaller than the right, and call this the canonical representation. All equivalent trees have exactly one canonical representation.

**Algorithm**

We can use a depth-first search to compare the canonical representation of each tree. If the traversals are the same, the representations are equal.

When traversing, we should be careful to encode both when we enter or leave a node.

```python
class Solution:
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))
```

**Complexity Analysis**

* Time Complexity: $O(N_1 + N_2)$, where $N_1, N_2$ are the lengths of `root1` and `root2`. (In Python, this is $\min(N_1, N_2)$.)

* Space Complexity: $O(N_1 + N_2)$. (In Python, this is $\min(H_1, H_2)$, where $H_1, H_2$ are the heights of the trees of `root1` and `root2`.)

# Submissions
---
**Solution:**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))
```

**Solution:**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))
```