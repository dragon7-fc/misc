95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique **BST**'s (binary search trees) that store values 1 ... n.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Submissions:
---
**Solution 1:**
```
Runtime: 68 ms
Memory Usage: 15.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def cTree(self,nums):
        if not nums:
            return [None]
        temp = []
        for i in range(len(nums)):
            for lnode in self.cTree(nums[:i]):
                for rnode in self.cTree(nums[i+1:]):
                    root = TreeNode(nums[i])
                    root.left = lnode
                    root.right = rnode
                    temp.append(root)
        return temp
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.cTree(list(range(1,n+1)))
```