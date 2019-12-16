116. Populating Next Right Pointers in Each Node

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

 

**Follow up:**

* You may only use constant extra space.
* Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:

![116_sample.png](img/116_sample.png)
```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Constraints:**

* The number of nodes in the given tree is less than `4096`.
* `-1000 <= node.val <= 1000`

# Submissions
---
**Solution 1:**
```
Runtime: 64 ms
Memory Usage: 14.2 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not root:
                return
            if not node.left and not node.right:
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        return root
```

**Solution 2:**
```
Runtime: 52 ms
Memory Usage: 14.2 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        stack = [root]

        while stack != []:
            for i in range(0,len(stack)-1):
                stack[i].next = stack[i+1]
            new_stack = []
            for i in stack:
                if i.left:
                    new_stack.append(i.left)
                if i.right:
                    new_stack.append(i.right)
            stack = new_stack

        return root
```