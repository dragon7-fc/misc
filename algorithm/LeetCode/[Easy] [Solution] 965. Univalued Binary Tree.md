965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.

Return `true` if and only if the given tree is univalued.

 

**Example 1:**

![965_unival_bst_1.png](img/965_unival_bst_1.png)
```
Input: [1,1,1,1,1,null,1]
Output: true
```

**Example 2:**

![965_unival_bst_2.png](img/965_unival_bst_2.png)
```
Input: [2,2,2,5,2]
Output: false
```

**Note:**

* The number of nodes in the given tree will be in the range `[1, 100]`.
* Each node's value will be an integer in the range `[0, 99]`.

# Solution
---
## Approach 1: Depth-First Search
**Intuition and Algorithm**

Let's output all the values of the array. After, we can check that they are all equal.

To output all the values of the array, we perform a depth-first search.

```python
class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

**Intuition and Algorithm**

A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes.

We can write our function recursively. `left_correct` will represent that the left child is correct: ie., that it is univalued, and the root value is equal to the left child's value. `right_correct` will represent the same thing for the right child. We need both of these properties to be true.

```python
class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(H)$, where $H$ is the height of the given tree.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
```