1676. Lowest Common Ancestor of a Binary Tree IV

Given the `root` of a binary tree and an array of `TreeNode` objects `nodes`, return the lowest common ancestor (LCA) of **all the nodes** in `nodes`. All the nodes will exist in the tree, and all values of the tree's nodes are **unique**.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes `p1`, `p2`, ..., `pn` in a binary tree `T` is the lowest node that has every `pi` as a **descendant** (where we allow **a node to be a descendant of itself**) for every valid `i`". A **descendant** of a node `x` is a node `y` that is on the path from node `x` to some leaf node.

 

**Example 1:**

![1676_binarytree.png](img/1676_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
```

**Example 2:**

![1676_binarytree.png](img/1676_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.
```

**Example 3:**

![1676_binarytree.png](img/1676_binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 10^4]`.
* `-10^9 <= Node.val <= 10^9`
* All `Node.val` are **unique**.
* All `nodes[i]` will exist in the tree.
* All `nodes[i]` are distinct.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 116 ms
Memory Usage: 19.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        def dfs(root, nodes):
            if not root: return None

            if root in nodes:
                return root

            left = dfs(root.left, nodes)
            right = dfs(root.right, nodes)

            if left and right:
                return root

            if left: return left
            if right: return right
            return None
        
        return dfs(root, nodes)
```

**Solution 2: (DFS, set)**
```
Runtime: 68 ms
Memory: 44.2 MB
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
    TreeNode* dfs(TreeNode* node, unordered_set<TreeNode*> &st) {
        if (!node) {
            return nullptr;
        }
        if (st.count(node)) {
            return node;
        }
        TreeNode *left, *right;
        left = dfs(node->left, st);
        right = dfs(node->right, st);
        if (left && right) {
            return node;
        }
        if (left) {
            return left;
        }
        if (right) {
            return right;
        }
        return nullptr;
    }
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, vector<TreeNode*> &nodes) {
        unordered_set<TreeNode*> st(nodes.begin(), nodes.end());
        return dfs(root, st);
    }
};
```

**Solution 3: (DFS, Set)**
```
Runtime: 61 ms
Memory: 46.3 MB
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
    TreeNode *res = nullptr;
    int traverse(TreeNode* r, unordered_set<TreeNode*> &ns) {
        int match = r == nullptr ? 0 :
            ns.count(r) + traverse(r->left, ns) + traverse(r->right, ns);
        if (match == ns.size() && res == nullptr)
            res = r;
        return match;
    }    
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, vector<TreeNode*> &nodes) {
        unordered_set<TreeNode*> ns(begin(nodes), end(nodes));
        traverse(root, ns);
        return res;
    }
};
```
