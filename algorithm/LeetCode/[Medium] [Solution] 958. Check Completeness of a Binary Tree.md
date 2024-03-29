958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

**Definition of a complete binary tree from Wikipedia:**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

**Example 1:**

![958_complete-binary-tree-1.png](img/958_complete-binary-tree-1.png)
```
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

**Example 2:**

![958_complete-binary-tree-2.png](img/958_complete-binary-tree-2.png)
```
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

**Note:**

* The tree will have between `1` and `100` nodes.

# Solution
---
## Approach 1: Breadth First Search
**Intuition**

This problem reduces to two smaller problems: representing the "location" of each node as a `(depth, position)` pair, and formalizing what it means for nodes to all be left-justified.

If we have say, `4` nodes in a row with depth `3` and positions `0, 1, 2, 3`; and we want `8` new nodes in a row with depth `4` and positions `0, 1, 2, 3, 4, 5, 6, 7`; then we can see that the rule for going from a node to its left child is `(depth, position) -> (depth + 1, position * 2)`, and the rule for going from a node to its right child is `(depth, position) -> (depth + 1, position * 2 + 1)`. Then, our row at depth $d$ is completely filled if it has $2^{d-1}$ nodes, and all the nodes in the last level are left-justified when their positions take the form `0, 1, ...` in sequence with no gaps.

A cleaner way to represent depth and position is with a code: `1` will be the root node, and for any node with code v, the left child will be `2*v` and the right child will be `2*v + 1`. This is the scheme we will use. Under this scheme, our tree is complete if the codes take the form `1, 2, 3, ...` in sequence with no gaps.

**Algorithm**

At the root node, we will associate it with the code `1`. Then, for each node with code `v`, we will associate its left child with code `2 * v`, and its right child with code `2 * v + 1`.

We can find the codes of every node in the tree in "reading order" (top to bottom, left to right) sequence using a breadth first search. (We could also use a depth first search and sort the codes later.)

Then, we check that the codes are the sequence `1, 2, 3, ...` with no gaps. Actually, we only need to check that the last code is correct, since the last code is the largest value.

```python
class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)
```

# Submissions
---
**Solution:**
```
Runtime: 44 ms
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)     
```

**Solution 1: (BFS)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                break
            queue.extend([node.left, node.right])
        return not any(queue)
```

**Solution 2: (BFS)**
```
Runtime: 3 ms
Memory: 10.3 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        queue<TreeNode*> q;
        bool has_null = false;
        TreeNode *cur;
        q.push(root);
        while (!q.empty()) {
            cur = q.front();
            q.pop();
            if (!cur) {
                has_null = true;
            } else {
                if (has_null) {
                    return false;
                }
                q.push(cur->left);
                q.push(cur->right);
            }
        }
        return true;
    }
};
```
