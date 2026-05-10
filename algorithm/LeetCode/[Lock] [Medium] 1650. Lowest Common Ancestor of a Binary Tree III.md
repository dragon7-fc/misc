1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree `p` and `q`, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for `Node` is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

**Constraints:**

* The number of nodes in the tree is in the range `[2, 105]`.
* `-10^9 <= Node.val <= 10^9`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` exist in the tree.

# Submissions
---
**Solution 1: (Tree)**
```
Runtime: 68 ms
Memory Usage: 18.5 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ps = set()
        while p:
            ps.add(p)
            p = p.parent
        while q:
            if q in ps:
                return q
            q = q.parent
```

**Solution 2: (Tree, ChatGPT, finding intersection of two singly linked lists)**

case1:
        3 <ans
       / \
   p> 5   1 <q
     / \ / \
    6  2 0  8
      / \
     7   4

p = 5
q = 1

answer: 3

case2:
        3
       / \
      5   1 <q
     /
 p> 6

p = 6
q = 1

a: 6 -> 5 ->    3 -> null -> 1 -> 3
                                  ^
                                  v
b: 1 -> 3 -> null ->    6 -> 5 -> 3


general:
p -> ... -> LCA -> ... -> root
  ------------- ----------------
       la             c
q -> ... -> LCA -> ... -> root
  ------------- ----------------
       lb             c

la + c + lb + c = lb + c + la + c
-> intersect


```c++
class Solution {
public:

    Node* lowestCommonAncestor(Node* p, Node* q) {

        Node* a = p;
        Node* b = q;

        while (a != b) {

            a = (a == nullptr) ? q : a->parent;
            b = (b == nullptr) ? p : b->parent;
        }

        return a;
    }
};
```
