114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
The flattened tree should look like:
```
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
```

# Submissions
---
**Solution 1: (Post-Order)**
```
Runtime: 32 ms
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
    prev = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
```

**Solution 2: (Stack)**
```
Runtime: 40 ms
Memory Usage: 15.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)    
            if node.left is not None:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
            node.left = None
```

**Solution 3: (DFS, right-left traversal)**
```
Runtime: 6 ms
Memory Usage: 6.9 MB
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

void dfs(struct TreeNode *node, struct TreeNode **prev) {
    if (!node)
        return;
    dfs(node->right, prev);
    dfs(node->left, prev);
    node->right = *prev;
    node->left = NULL;
    *prev = node;
}

void flatten(struct TreeNode* root){
    struct TreeNode *prev = NULL;
    dfs(root, &prev);
    return root;
}
```

**Solution 4: (DFS, preorder)**
```
Runtime: 4 ms
Memory Usage: 6.9 MB
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

void dfs(struct TreeNode *node, struct TreeNode **prev) {
    if (!node)
        return;
    struct TreeNode *right = node->right;
    if (*prev)
        (*prev)->right = node;
    *prev = node;
    dfs(node->left, prev);
    dfs(right, prev);
    node->left = NULL;
}

void flatten(struct TreeNode* root){
    struct TreeNode *prev = NULL;
    dfs(root, &prev);
    return root;
}
```
