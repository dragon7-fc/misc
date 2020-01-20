515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

**Example:**
```
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
```

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 36 ms
Memory Usage: 14.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        level = root and [root]
        ans = []
        while level:
            ans.append(max([node.val for node in level]))
            level = [c for node in level for c in [node.left, node.right] if c]
        return ans
```