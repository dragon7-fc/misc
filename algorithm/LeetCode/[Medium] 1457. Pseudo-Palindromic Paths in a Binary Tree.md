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
**Solution 1: (DFS, Bit Manipulations)**

1. Count the frequencies of same numbers in each path, if there are at most 1 frequency is odd, then it is a valid path;
1. Use the 0th to 9th bit s of a int to record the odd/even frequency in a path, since the numbers range from 0 ~ 9;
```
Runtime: 356 ms
Memory Usage: 49.5 MB
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
        
        def dfs(node, cnt) :
            if not node:
                return 0
            cnt ^= 1 << node.val
            if not node.left and not node.right:
                return 0 if bin(cnt).count('1') > 1 else 1
            return dfs(node.left, cnt) + dfs(node.right, cnt)
            
        return dfs(root, 0)
```