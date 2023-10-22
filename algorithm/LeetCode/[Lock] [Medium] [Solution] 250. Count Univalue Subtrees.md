250. Count Univalue Subtrees

Given the `root` of a binary tree, return the number of **uni-value** subtrees.

A **uni-value subtree** means all nodes of the subtree have the same value.

 

**Example 1:**

![250_unival_e1.jpg](img/250_unival_e1.jpg)
```
Input: root = [5,1,5,5,5,null,5]
Output: 4
```

**Example 2:**
```
Input: root = []
Output: 0
```

**Example 3:**
```
Input: root = [5,5,5,5,5,null,5]
Output: 6
```

**Constraints:**

* The numbrt of the node in the tree will be in the range `[0, 1000]`.
* `-1000 <= Node.val <= 1000`

# Submissions
---
**Solution 1: (Depth First Search)**
```
Runtime: 32 ms
Memory Usage: 14.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:

            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni
```

**Solution 2: (Depth First Search - Pass Parent Values)**
```
Runtime: 24 ms
Memory Usage: 14.5 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count


    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val
```

**Solution 3: (DFS)**
```
Runtime: 0 ms
Memory: 16.7 MB
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
    pair<bool, int> dfs(TreeNode* node) {
        if (!node) {
            return {true, 0};
        }

        auto left = dfs(node->left);
        auto right = dfs(node->right);
        bool isLeftUniValue = left.first;
        bool isRightUniValue = right.first;
        int count = left.second + right.second;

        // If both the children form uni-value subtrees, we compare the value of
        // chidrens node with the node value.
        if (isLeftUniValue && isRightUniValue) {
            if (node->left && node->val != node->left->val) {
                return {false, count};
            }
            if (node->right && node->val != node->right->val) {
                return {false, count};
            }
            return {true, count + 1};
        }
        // Else if any of the child does not form a uni-value subtree, the subtree
        // rooted at node cannot be a uni-value subtree.
        return {false, count};
    }
public:
    int countUnivalSubtrees(TreeNode* root) {
        return dfs(root).second;
    }
};
```
