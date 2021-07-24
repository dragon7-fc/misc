814. Binary Tree Pruning

We are given the head node `root` of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

**Example 1:**
```
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```
![814_1028_2.png](img/814_1028_2.png)

**Example 2:**
```
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```
![814_1028_1.png](img/814_1028_1.png)

**Example 3:**
```
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```
![814_1028.png](img/814_1028.png)

**Note:**

* The binary tree will have at most `100` nodes.
* The value of each node will only be `0` or `1`.

# Solution
---
## Approach #1: Recursion [Accepted]
**Intuition**

Prune children of the tree recursively. The only decisions at each node are whether to prune the left child or the right child.

Algorithm

We'll use a function `containsOne(node)` that does two things: it tells us whether the subtree at this node contains a 1, and it also prunes all subtrees not containing 1.

If for example, `node.left` does not contain a one, then we should prune it via node.`left = null`.

Also, the parent needs to be checked. If for example the tree is a single node `0`, the answer is an empty tree.

```python
class Solution(object):
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the tree. We process each node once.

* Space Complexity: $O(H)$, where $H$ is the height of the tree. This represents the size of the implicit call stack in our recursion.

# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contains_one(node: TreeNode) -> bool:
            if not node: 
                return False
            
            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)
            
            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)
            
            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one: 
                node.left = None
                
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one: 
                node.right = None
            
            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None
```
