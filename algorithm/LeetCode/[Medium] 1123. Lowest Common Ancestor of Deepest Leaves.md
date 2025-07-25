1123. Lowest Common Ancestor of Deepest Leaves

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

* The node of a binary tree is a leaf if and only if it has no children
* The depth of the root of the tree is `0`, and if the depth of a node is `d`, the depth of each of its children is `d+1`.
* The lowest common ancestor of a set `S` of nodes is the node `A` with the largest depth such that every node in `S` is in the subtree with root `A`.
 

**Example 1:**
```
Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
```

**Example 2:**
```
Input: root = [1,2,3,4]
Output: [4]
```

**Example 3:**
```
Input: root = [1,2,3,4,5]
Output: [2,4,5]
```

**Constraints:**

* The given tree will have between `1` and `1000` nodes.
* Each node of the tree will have a distinct value between `1` and `1000`.

**Note:** This question is the same as 865: [https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

# Submissions
---
**Solution 1:**
```
Runtime: 48 ms
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
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.max_depth = 0
        self.lca = None
        
        def dfs(node, depth=0):
            if node is None:
                return -1
            
            if node.left is None and node.right is None:
                if depth > self.max_depth:
					# The depth of the current leaf is deeper than the depth of all leaves encountered so far.
					# -> Update max_depth and LCA.
                    self.max_depth = depth
                    self.lca = node   
                return depth
              
			# Post-order traversal: get depth of left and right subtree
            res_l = dfs(node.left, depth+1)
            res_r = dfs(node.right, depth+1)
            
			# If left and right subtree contain a deepest leaf, the current node is an LCA candidate.
            if res_l == self.max_depth and res_r == self.max_depth:
                self.lca = node

            return max(res_l,res_r)
        
        dfs(root)
        return self.lca
            
        
```

**Solution 2: (DFS)**
```
Runtime: 16 ms
Memory Usage: 8.6 MB
```
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* helper(struct TreeNode* root, int* level)
{
    int left=0,right=0;
    struct TreeNode* leftNode=NULL,*rightNode=NULL;
    
    if(root==NULL)
    {
        *level = 0;
        return NULL;
    }
    leftNode = helper(root->left, &left);
    rightNode = helper(root->right, &right);
    
    if(left == right)
    {
        *level = left + 1;
        return root;
    }
    else if(left < right)
    {
        *level = right + 1;
        return rightNode;
    }
    else
    {
        *level = left + 1;
        return leftNode;
    }
}

struct TreeNode* lcaDeepestLeaves(struct TreeNode* root){
    int level = 0;
    return helper(root, &level);
}
```

**Solution 3: (DFS)**

        0
       /  \
      1    3
       \
        2 <

```
Runtime: 0 ms, Beats 100.00%
Memory: 23.14 MB, Beats 16.07%
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
    pair<int,TreeNode*> dfs(TreeNode *node, int d) {
        if (!node) {
            return {-1, nullptr};
        }
        if (!node->left && !node->right) {
            return {d, node};
        }
        auto [left, lnode] = dfs(node->left, d+1);
        auto [right, rnode] = dfs(node->right, d+1);
        if (left == right) {
            return {max(left, d), node};
        } else if (left > right) {
            return {left, lnode};
        } else {
            return {right, rnode};
        }
    }
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root, 0).second;
    }
};
```
