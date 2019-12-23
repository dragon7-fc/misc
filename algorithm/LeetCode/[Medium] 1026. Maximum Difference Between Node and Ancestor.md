1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value `V` for which there exists **different** nodes `A` and `B` where `V = |A.val - B.val|` and `A` is an ancestor of `B`.

(A node `A` is an ancestor of `B` if either: any child of `A` is equal to `B`, or any child of `A` is an ancestor of `B`.)

 

**Example 1:**

![1026_2whqcep.jpg](img/1026_2whqcep.jpg)
```
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Note:**

* The number of nodes in the tree is between `2` and `5000`.
* Each node will have value between `0` and `100000`.

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 18.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, minVal, maxVal):
            if not node:
                return 0

            maxDiff = max(abs(node.val - minVal), abs(node.val - maxVal))
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            left_maxDiff = dfs(node.left, minVal, maxVal)
            right_maxDiff = dfs(node.right, minVal, maxVal)

            return max(maxDiff, left_maxDiff, right_maxDiff)
        
        return dfs(root, root.val, root.val)
```