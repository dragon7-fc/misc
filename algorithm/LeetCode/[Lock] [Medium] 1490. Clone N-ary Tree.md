1490. Clone N-ary Tree

Given a `root` of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (`int`) and a list (`List[Node]`) of its children.
```
class Node {
    public int val;
    public List<Node> children;
}
```

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

**Example 1:**

![1490_narytreeexample.png](img/1490_narytreeexample.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

**Example 2:**

![1490_sample_4_964.png](img/1490_sample_4_964.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

**Constraints:**

* The depth of the n-ary tree is less than or equal to `1000`.
* The total number of nodes is between `[0, 104]`.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 123 ms
Memory Usage: 18.2 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        d = {}
        q = [root]
        d[root] = Node(root.val)
        while q:
            nq = []
            for node in q:
                for c in node.children:
                    if c:
                        d[c] = Node(c.val)
                        d[node].children += [d[c]]
                        nq += [c]
            q = nq
            
        return d[root]
```
