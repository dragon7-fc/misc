1457. Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from `1` to `9`. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.

Return the number of **pseudo-palindromic** paths going from the root node to leaf nodes.

 

**Example 1:**

![1457_palindromic_paths_1.png](img/1457_palindromic_paths_1.png)
```
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 2:**

![1457_palindromic_paths_2.png](img/1457_palindromic_paths_2.png)
```
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 3:**
```
Input: root = [9]
Output: 1
```

**Constraints:**

* The given binary tree will have between `1` and `10^5` nodes.
* Node values are digits from `1` to `9`.

# Submissions
---
**Solution 1: (Iterative Preorder Traversal)**
```
Runtime: 332 ms
Memory Usage: 50 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        count = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return count
```

**Solution 2: (Recursive Preorder Traversal)**
```
Runtime: 324 ms
Memory Usage: 49.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:                    
                    preorder(node.left, path)
                    preorder(node.right, path) 
        
        count = 0
        preorder(root, 0)
        return count
```

**Solution 3: (Backtracking)**
```
Runtime: 636 ms
Memory Usage: 178.5 MB
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
    int ans = 0;
    void preorder(TreeNode* node, int cnt) {
        if (node == NULL) return;
        cnt ^= (1 << node->val);
        if (!node->left && !node->right) {
            ans += (cnt & (cnt - 1)) == 0;
        }
        preorder(node->left, cnt);
        preorder(node->right, cnt);
    }
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        preorder(root, 0);
        return ans;
    }
};
```
