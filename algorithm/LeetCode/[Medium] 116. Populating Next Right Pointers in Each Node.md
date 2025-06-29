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
**Solution 1: (DFS)**
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

**Solution 2: (BFS)**
```
Runtime: 60 ms
Memory Usage: 15.4 MB
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
        q = [root] if root else []
        while q:
            nq = []
            n = len(q)
            for i in range(len(q)):
                if i != n-1:
                    q[i].next = q[i+1]
                if q[i].left:
                    nq += [q[i].left, q[i].right]
            q = nq
            
        return root
```

**Solution 3: (BFS)**
```
Runtime: 64 ms
Memory Usage: 15.6 MB
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
        q = [root] if root else []
        while q:
            nq = [c for node in q for c in [node.left, node.right] if c]
            for i, node in enumerate(nq):
                if i != len(nq)-1:
                    node.next = nq[i+1]
            q = nq
                
        return root
```

**Solution 4: (BFS)**
```
Runtime: 20 ms
Memory Usage: 17.3 MB
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(!root)
            return root;
        queue<Node*> q;
        q.push(root);
        while(!q.empty())
        {
           int n =q.size();
           while(n--)
           {
               Node* x = q.front();
               q.pop();
               x->next = n == 0 ? NULL :q.front();
               if(x->left)
                   q.push(x->left);
               if(x->right)
                   q.push(x->right);
           }
        }
        return root;
    }
};
```

**Solution 5: (DFS)**
```
Runtime: 19 ms
Memory Usage: 9 MB
```
```c
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *left;
 *     struct Node *right;
 *     struct Node *next;
 * };
 */
void dfs(struct Node* node) {
    if (!node || !node->left && !node->right)
        return;
    node->left->next = node->right;
    if (node->next)
        node->right->next = node->next->left;
    dfs(node->left);
    dfs(node->right);
}

struct Node* connect(struct Node* root) {
	dfs(root);
    return root;
}
```

**Solution 6: (BFS)**
```
Runtime: 14 ms, Beats 53.16%
Memory: 19.26 MB, Beats 40.23%
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        int i, sz;
        queue<Node*> q;
        Node *pre;
        if (root) {
            q.push(root);
        }
        while (q.size()) {
            sz = q.size();
            pre = nullptr;
            for (i = 0; i < sz; i ++) {
                auto node = q.front();
                q.pop();
                if (pre) {
                    pre->next = node;
                }
                pre = node;
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};
```
