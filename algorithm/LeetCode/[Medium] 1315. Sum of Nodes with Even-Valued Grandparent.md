1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return `0`.

 

**Example 1:**

![1315_1473_ex1.png](img/1315_1473_ex1.png)
```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
```

**Constraints:**

* The number of nodes in the tree is between `1` and `10^4`.
* The value of nodes is between `1` and `100`.

# Submissions
---
**Solution 1:**

Bind the parent node with the even/odd flag of grand parent.

```
Runtime: 104 ms
Memory Usage: 16.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans, dq = 0, collections.deque([(root, False)])
        while dq:
            parent, evenGrandParent = dq.popleft()
            evenParent = parent.val % 2 == 0
            for child in parent.left, parent.right:
                if child:
                    dq.append((child, evenParent))
                    ans += child.val if evenGrandParent else 0
        return ans
```

**Solution 2: (DFS, post-order)**
```
Runtime: 255 ms
Memory: 18 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return [0, 0]
            left_one, left_two = dfs(node.left)
            right_one, right_two = dfs(node.right)
            if node.val%2 == 0:
                ans += left_two + right_two
            return [node.val, left_one + right_one]
        
        dfs(root)
        return ans
```
