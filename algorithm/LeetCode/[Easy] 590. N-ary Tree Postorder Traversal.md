590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

 

**Example 1:**

![590_narytreeexample.png](img/590_narytreeexample.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

**Example 2:**

![590_sample_4_964.png](img/590_sample_4_964.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
``` 

**Constraints:**

* The height of the n-ary tree is less than or equal to `1000`
* The total number of nodes is between `[0, 10^4]`

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
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
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            for c in node.children:
                dfs(c)
            self.ans.append(node.val)
        dfs(root)
        return self.ans
```

**Solution 2:**
```
Runtime: 48 ms
Memory Usage: 14.6 MB
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
    def postorder(self, root: 'Node') -> List[int]:
        ans = collections.deque([])
        stack = root and [root]
        while stack:
            node = stack.pop()
            ans.appendleft(node.val)
            stack.extend([c for c in node.children if c])
        return ans
```