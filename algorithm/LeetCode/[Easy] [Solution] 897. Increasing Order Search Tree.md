897. Increasing Order Search Tree

Given a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

**Example 1:**
```
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
```

**Note:**

1. The number of nodes in the given tree will be between `1` and `100`.
1. Each node will have a unique integer value from `0` to `1000`.

# Solution
---
## Approach 1: In-Order Traversal
**Intuition**

The definition of a binary search tree is that for every node, all the values of the left branch are less than the value at the root, and all the values of the right branch are greater than the value at the root.

Because of this, an in-order traversal of the nodes will yield all the values in increasing order.

**Algorithm**

Once we have traversed all the nodes in increasing order, we can construct new nodes using those values to form the answer.

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$, the size of the answer.

## Approach 2: Traversal with Relinking
**Intuition and Algorithm**

We can perform the same in-order traversal as in Approach 1. During the traversal, we'll construct the answer on the fly, reusing the nodes of the given tree by cutting their left child and adjoining them to the answer.

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(H)$ in additional space complexity, where $H$ is the height of the given tree, and the size of the implicit call stack in our in-order traversal.

# Submissions
---
**Solution: (Traversal with Relinking)**
```
Runtime: 88 ms
Memory Usage: 13 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```

**Solution 1: (DFS)**
```
Runtime: 3 ms
Memory Usage: 7.6 MB
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
    void dfs(TreeNode* node, TreeNode* &p, TreeNode* &ans) {
        if (!node)
            return;
        dfs(node->left, p, ans);
        if (!ans)
            ans = node;
        if (p)
            p->right = node;
        node->left = nullptr;
        p = node;
        dfs(node->right, p, ans);
    }
public:
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode *parent = nullptr, *ans = nullptr;
        dfs(root, parent, ans);
        return ans;
    }
};
```
