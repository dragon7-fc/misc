255. Verify Preorder Sequence in Binary Search Tree

Given an array of **unique** integers `preorder`, return `true` if it is the correct preorder traversal sequence of a binary search tree.

 

**Example 1:**

![255_preorder-tree.jpg](img/255_preorder-tree.jpg)
```
Input: preorder = [5,2,1,3,6]
Output: true
```

**Example 2:**
```
Input: preorder = [5,2,6,1,3]
Output: false
```

**Constraints:**

* `1 <= preorder.length <= 10^4`
* `1 <= preorder[i] <= 10^4`
* All the elements of `preorder` are **unique**.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 391 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stck, lo, n = [], -float('inf'), len(preorder)
        for i in range(n):
            if preorder[i] < lo:
                return False
            if i > 0 and preorder[i] > preorder[i-1]:  # update min threshold
                while stck and stck[-1] < preorder[i]:
                    lo = stck.pop()
            stck.append(preorder[i])
        return True
```
